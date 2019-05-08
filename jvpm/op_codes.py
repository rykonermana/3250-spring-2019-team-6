"""This class defines a method for operational codes that java virtual machine uses"""
import csv
import numpy
from jvpm.class_file import *
from jvpm.utils import NONE, T_INT, T_LONG, T_FLOAT, T_DOUBLE, T_OBJECT, DIRECTORY,\
    parse_bytes_value


class OpCodes:
    """This class defines a method for operational codes that java virtual machine uses"""

    def __init__(self, class_ref=None, opcodes=[]):
        """Initiate variables"""
        self.table = self.load()
        self.stack = []
        self.localvar = [0] * 10
        self.opcode_list = opcodes
        self.class_ref = class_ref
        self.type = NONE

    def load(self):
        """Fills a dictionary with the bytecodes of different operational codes"""
        with open(DIRECTORY + 'jvpm/files/int_opcodes.csv', 'r') as csvfile:
            dict1 = {}
            spam_reader = csv.DictReader(csvfile)
            for ind in list(spam_reader):
                opcode_info = {'name': ind['name'].strip(),
                               'method':ind['method'].strip(),
                               'num_initial_bytes': int(ind['num_initial_bytes'].strip()),
                               'type': int(ind['type'])}
                the_number = int(ind['opcode'].strip(), 16)
                dict1[the_number] = opcode_info
        return dict1

    def run(self):
        """"Runs method associated with opcode"""
        for opcode_and_params in self.opcode_list:
            opcode = opcode_and_params['opcode']
            self.type = self.table[opcode]['type']
            if self.table[opcode]['num_initial_bytes'] > 0:
                value = opcode_and_params['message']
                getattr(self, self.table[opcode]['method'])(value)
            else:
                getattr(self, self.table[opcode]['method'])()

    def not_implemented(self):
        """Called when a certain element of the program is not yet implemented"""
        raise NotImplementedError("This function is not implemented.")

    ############################## PUSH TO STACK METHODS ###########################################

    def push_to_stack(self, val):
        """Method to push the correct style variable to the stack"""
        if self.type == T_INT:
            self.push_int_to_stack(val)
        elif self.type == T_LONG:
            self.push_long_to_stack(val)
        elif self.type == T_FLOAT:
            self.push_float_to_stack(val)
        elif self.type == T_DOUBLE or self.type == T_OBJECT:
            self.stack.append(val)

    def pop_from_stack(self):
        """Method to pop the correct style variable to the stack"""
        if self.type == T_LONG:
            return self.pop_long_from_stack()
        if self.type == T_INT:
            return self.stack.pop()
        if self.type == T_FLOAT:
            return self.pop_float_from_stack()
        # else:
        return self.stack.pop()

    def push_int_to_stack(self, value):
        """Method to check if python is attempting to push a 64 bit integer which is
        not allowed in java"""
        extreme_value = 2147483647
        low_extreme_value = -2147483648
        if value > extreme_value or value < low_extreme_value:
            raise ValueError()
        self.stack.append(value)

    def push_float_to_stack(self, value):
        """Method to push a float value that is first checked if it is in the allowable range"""
        extreme_value = 2147483647
        low_extreme_value = -2147483648
        if value > extreme_value or value < low_extreme_value:
            raise ValueError()
        self.stack.append(numpy.float32(value))

    def pop_float_from_stack(self):
        """Method to pop a float value that is first checked if it is in the allowable range"""
        value = self.stack.pop()
        extreme_value = 2147483647
        low_extreme_value = -2147483648
        if value > extreme_value or value < low_extreme_value:
            raise ValueError("Invalid float")
        return numpy.float32(value)

    def push_long_to_stack(self, word):
        """Method to pop a float value that is first checked if it is in the allowable range"""
        negative = 1
        if word > 2 ** 63 - 1 or word < -(2 ** 63):
            raise ValueError("long is too big or small")
        if word < 0:
            negative = -1
            word *= -1
        self.stack.append(negative * self.extract_lower_bits(word))
        self.stack.append(negative * self.extract_upper_bits(word))

    def pop_long_from_stack(self):
        """Method to pop a long variable from a stack that would take two stack blocks in java"""
        upper_bits = self.stack.pop()
        lower_bits = self.stack.pop()
        negative = 1
        if upper_bits < 0 or lower_bits < 0:
            negative = -1
        shift_amount = 32
        upper_bits = abs(upper_bits) << shift_amount
        binary_word = (abs(lower_bits) + upper_bits) * negative
        return binary_word

    def extract_upper_bits(self, word):
        """Method to get the highest value 32 bits of a 64-bit value"""
        bit_screen = 0x7FFFFFFF00000000
        shift_amount = 32
        return (int(word) & bit_screen) >> shift_amount

    def extract_lower_bits(self, word):
        """Method to get the lowest value 32 bits of a 64-bit value"""
        bit_screen = 0x00000000FFFFFFFF
        return int(word) & bit_screen

    ## start primitive type opcodes ##########################################################

    def add(self):
        """Adds two numbers in a stack and pushes the result back on"""
        self.push_to_stack(self.pop_from_stack() + self.pop_from_stack())

    def opcode_and(self):
        """Pushes the result of the operation 'and' of two numbers in the stack"""
        val1 = self.pop_from_stack() #to clear up sonarcloud smells
        val2 = self.pop_from_stack()
        self.push_to_stack(val1 & val2)

    def const_m1(self):
        """Pushes '-1' onto the stack"""
        m_number = -1
        self.push_to_stack(m_number)

    def const_0(self):
        """Pushes '0' unto the stack"""
        m_number = 0
        self.push_to_stack(m_number)

    def const_1(self):
        """pushes '1' unto the stack"""
        m_number = 1
        self.push_to_stack(m_number)

    def const_2(self):
        """Pushes '2' unto the stack"""
        m_number = 2
        self.push_to_stack(m_number)

    def const_3(self):
        """Pushes '3' unto the stack"""
        m_number = 3
        self.push_to_stack(m_number)

    def const_4(self):
        """Pushes '4' unto the stack"""
        m_number = 4
        self.push_to_stack(m_number)

    def const_5(self):
        """Pushes '5' unto the stack"""
        m_number = 5
        self.push_to_stack(m_number)

    def div(self):
        """Pushes the result of the second number in the stack divided by the next
         number in the stack"""
        numerator = self.pop_from_stack()
        denomenator = self.pop_from_stack()
        if denomenator != 0:
            word = numerator / denomenator
            self.push_to_stack(word)
        else:
            raise ZeroDivisionError("Divided by Zero")

    def mul(self):
        """Pushes the result of the top two numbers in the stack"""
        self.push_to_stack(self.pop_from_stack() * self.pop_from_stack())

    def neg(self):
        """Pushes the next number in the stack multiplied by '-1'"""
        val = self.pop_from_stack() * (-1)
        self.push_to_stack(val)

    def opcode_or(self):
        """Pushes the result of the operation 'or' of two numbers in the stack"""
        val1 = self.pop_from_stack()
        val2 = self.pop_from_stack()
        self.push_to_stack(val1 | val2)

    def rem(self):
        """Pushes the remainder of the second number in the stack divided by the next number"""
        val1 = self.pop_from_stack()
        val2 = self.pop_from_stack()
        self.push_to_stack(val1 % val2)

    def shl(self):
        """Pushes the result of the second number in the stack with it's bytes shifted left
        by the amount of the next number in the stack"""
        val = self.pop_from_stack()
        temp_type = self.type
        self.type = T_INT
        shift = self.pop_from_stack()
        val = val << shift
        self.type = temp_type
        self.push_to_stack(val)

    def shr(self):
        """Pushes the result of the second number in the stack with it's bytes shifted right
        by the amount of the next number in the stack"""
        val = self.pop_from_stack()
        temp_type = self.type
        self.type = T_INT
        shift = self.pop_from_stack()
        val = val >> shift
        self.type = temp_type
        self.push_to_stack(val)

    def sub(self):
        """Pushes the result of the second number in the stack minus the next number"""
        val1 = self.pop_from_stack() # to clear up sonarcloud smells
        val2 = self.pop_from_stack()
        self.push_to_stack(val1 - val2)

    def ushr(self):
        """Pushes the result of the second number in the stack with it's bytes shifted right
        arithmetically by the amount of the next number in the stack"""
        m_number = 0x100000000
        self.push_to_stack((self.pop_from_stack() % m_number) >> self.pop_from_stack())

    def xor(self):
        """Pushes the result of the operation 'exclusive or' of two numbers in the stack"""
        val1 = self.pop_from_stack() # to clear up sonarcloud smells
        val2 = self.pop_from_stack()
        self.push_to_stack(val1 ^ val2)

    def load_0(self):
        """Loads the variable of the variable array 'index 0' unto the stack"""
        index = 0
        self.push_to_stack(self.localvar[index])

    def load_1(self):
        """Loads the variable of the variable array 'index 1' unto the stack"""
        index = 1
        self.push_to_stack(self.localvar[index])

    def load_2(self):
        """Loads the variable of the variable array 'index 2' unto the stack"""
        index = 2
        self.push_to_stack(self.localvar[index])

    def load_3(self):
        """Loads the variable of the variable array 'index 3' unto the stack"""
        index = 3
        self.push_to_stack(self.localvar[index])

    def store_0(self):
        """Stores the next number in the stack onto the variable array on 'index 0'"""
        index = 0
        self.localvar[index] = self.pop_from_stack()

    def store_1(self):
        """Stores the next number in the stack onto the variable array on 'index 1'"""
        index = 1
        self.localvar[index] = self.pop_from_stack()

    def store_2(self):
        """Stores the next number in the stack onto the variable array on 'index 2'"""
        index = 2
        self.localvar[index] = self.pop_from_stack()

    def store_3(self):
        """Stores the next number in the stack onto the variable array on 'index 3'"""
        index = 3
        self.localvar[index] = self.pop_from_stack()

    def convert(self, to_type):
        """Calls on a method depending on the type to convert a value to that type"""
        val = self.pop_from_stack()
        self.type = to_type
        self.push_to_stack(val)

    def convert_double(self):
        """Converts value to double"""
        self.convert(T_DOUBLE)

    def convert_int(self):
        """Converts value to integer"""
        self.convert(T_INT)

    def convert_long(self):
        """Converts value to long"""
        self.convert(T_LONG)

    def convert_float(self):
        """Converts value to float"""
        self.convert(T_FLOAT)

    def convert_byte(self):
        """Pushes the next number in the stack as a byte reference"""
        self.stack.append(self.pop_from_stack().to_bytes(
            length=1, byteorder='big', signed=True))

    def convert_char(self):
        """Pushes the next number in the stack as a character reference"""
        self.stack.append(chr(self.pop_from_stack()))

    def convert_short(self):
        """Converts a value to a short if within the allowable range"""
        op_max = 2 ** 16 - 1
        op_min = -2 ** 16
        m_number = 1.0
        value = self.pop_from_stack()
        if op_min <= value <= op_max:
            self.stack.append(value / m_number)
        else:
            raise ValueError(
                "Value {} cannot be converted to short".format(value))

    def ldc(self, index):
        """Pushes constant index to stack"""
        self.type = T_OBJECT
        constant_number = parse_bytes_value(index, 0, 1)
        self.push_to_stack(self.class_ref.constant_table.get_constant(constant_number))

    def invoke_special(self, bytes_constant):
        """Method that pushes the method string to the stack"""
        constant_number = parse_bytes_value(bytes_constant, 0, 2)
        method_string = self.class_ref.constant_table.get_constant(constant_number)
        self.push_to_stack(method_string)

    def invoke_virtual_helper(self, bytes_constant):
        """invokes the correct virtual method with the method string"""
        constant_number = parse_bytes_value(bytes_constant, 0, 2)
        method_string = self.class_ref.constant_table.get_constant(constant_number)
        self.invoke_virtual(method_string)

    def invoke_virtual(self, method_ref):
        """Method for reading a java invoke virtual method and applying the correct method
        from python"""
        invoke = {"java/io/PrintStream.println:(I)V": "print_primitive",
                  "java/io/PrintStream.println:(Z)V": "print_boolean",
                  "Method java/io/PrintStream.println:(D)V": "print_double",
                  "java/io/PrintStream.println:(Ljava/lang/String;)V": "print_primitive",
                  "java/util/Scanner.nextString:()Ljava.lang/String": "input_string",
                  "java/util/Scanner.nextInt:()I": "input_int",
                  "java/util/Scanner.nextDouble:()D": "input_double"}
        if method_ref in invoke:
            return getattr(self, invoke[method_ref])()
        # else
        self.not_implemented()

    def print_boolean(self):
        """Is called when invokeVirtual method is called to print an boolean"""
        self.type = T_INT
        num = self.stack.pop()
        if num == 1:
            print("true")
            return "true"
        if num == 0:
            print("false")
            return "false"
        # else
        raise TypeError("Value couldn't be interpreted as a boolean.")

    def print_double(self):
        """Is called when invokedVirtual method is called to print a double"""
        self.type = T_DOUBLE
        m_number = self.pop_from_stack()
        print(m_number)
        return m_number

    def print_primitive(self):
        """Is called to print a primitive value"""
        self.type = T_OBJECT
        val = self.pop_from_stack()
        print(val)
        return val

    def input_string(self):
        """Takes input as a string"""
        val = str(input())
        self.type = T_OBJECT
        self.push_to_stack(val)
        return val

    def input_int(self):
        """Takes input as an integer"""
        val = int(input())
        self.type = T_INT
        self.push_to_stack(val)
        return val

    def input_double(self):
        """Takes input as a float/double"""
        val = float(input())
        self.type = T_DOUBLE
        return val

    def do_nothing(self, args=[]):
        """called by opcodes that aren't required in python
        """
