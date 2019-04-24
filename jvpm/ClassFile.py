"""This program runs a java virtual machine using python"""
import unittest
import csv
import struct
import numpy

from .constant_table import ConstantTable
from .method_table import MethodTable

# unittest

NONE, T_INT, T_LONG, T_FLOAT, T_DOUBLE = 0, 1, 2 ,3, 4

class ClassFile():
    """Main file of the java python virtual machine"""

    def __init__(self, file='jvpm/files/HelloWorld.class'):
        with open(file, 'rb') as binary_file:
            # the byte string being stored in self.data to be parsed
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            self.constant_pool_count = self.get_constant_pool()-1
            self.constant_table = ConstantTable(
                self.data, self.constant_pool_count)
            self.constant_pool_length = self.constant_table.final_byte
            # self.access_flags = self.get_access_flags()
            # self.this_class = self.get_this_class()
            # self.superclass = self.get_super_class()
            # self.interface_count = self.get_interface_count()
            # self.cp_and_ic = self.interface_count + self.constant_table['length']
            # self.interface_table = self.get_interface_table()
            # self.field_count = self.get_field_count()
            # self.cp_ic_fc = 224 #  = self.cp_and_ic + self.field_count
            # self.field_table = self.get_field_table()
            # self.method_count = self.get_method_count()
            # self.method_table = MethodTable(self.data,self.method_count,self.cp_ic_fc)
            # self.cp_ic_fc_mc = self.cp_ic_fc + len(self.method_table)
            # self.attribute_count = self.get_attribute_count()
            # self.attribute_table = self.get_attribute_table()

    def get_magic(self):
        """Finds the magic number in the byte code which confirms the following
         is java formatted byte code"""
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        """Returns the minor version number"""
        return self.data[4] + self.data[5]

    def get_major(self):
        """Returns the major version number"""
        return self.data[6] + self.data[7]

    def get_constant_pool(self):
        """Returns how large the constant pool is"""
        return self.data[8] + self.data[9]

    # def get_interface_count(self):
    #     return self.data[16 + self.constant_pool_length] + self.data[17
    #     + self.constant_pool_length]
    #
    # def get_interface_table(self):
    #     interface = ""
    #     for i in range(self.interface_count):
    #         interface += format(self.data[i + 18 + self.constant_pool_length], '02X')
    #     return interface
    #
    # def get_field_count(self):
    #     return self.data[18 + self.cp_and_ic] + self.data[19 + self.cp_and_ic]

    # def get_field_table(self):
    #     field = self.data[self.cp_and_ic+20:(self.field_count+self.cp_ic_fc+20)]
    #     # for i in range(self.field_count):
    #     #    field += format(self.data[i + 20 + self.cp_and_ic], '02X')
    #     return field

    def get_method_count(self):
        return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]

    # def get_attribute_count(self):
    #     return self.data[22 + self.cp_ic_fc_mc] + self.data[23 + self.cp_ic_fc_mc]

    # def get_attribute_table(self):
    #     attribute = self.data[(24+self.cp_ic_fc_mc):(24+self.cp_ic_fc_mc+self.attribute_count)]
    #     # for i in range(self.attribute_count):
    #     #    attribute += format(self.data[i + 24 + self.cp_ic_fc_mc], '02X')
    #     return attribute

    def __str__(self):
        """Prints out to the console"""
        result = "{} {}".format("Magic:", self.magic)
        result += "{} {}\n{} {}\n{} {}\n{}".format("Minor version: ", self.minor,
                                                   "Major version: ", self.major,
                                                   "Constant pool count: ", self.constant_pool_count,
                                                   str(self.constant_table))
    #     print("Access flags: ", hex(self.access_flags[0]), hex(self.access_flags[1]))
    #     print("This class: ", self.this_class)
    #     print("Superclass: ", self.superclass)
    #     print("Interface count: ", self.interface_count)
    #     print("Cp + Ic: ", self.cp_and_ic)
    #     print("Field count: ", self.field_count)
    #     print("Cp + Ic + fc: ", self.cp_ic_fc)
    #     print("Field table: ", "[%s]" % ", ".join(map(str, self.field_table)))
    #     print("Method count: ", self.method_count)
    #     print("Cp + IC + Fc + Mc: ", self.cp_ic_fc_mc)
    #     print("Opcode table: ",''.join("%02x, "%i for i in self.method_table))
    #     print("Attribute count: ", self.attribute_count)
    #     print("Attribute table: ", "[%s]" % ", ".join(map(str, self.attribute_table)))
        return result

    def run_opcodes(self):
        """Runs the opcode class with the method table passed through it"""
        opcodes = OpCodes(self.method_table)
        opcodes.run()

class OpCodes:
    """This class defines a method for operational codes that java virtual machine uses"""

    def __init__(self, class_ref=ClassFile(), opcodes=[]):
        # {0x00: self.not_implemented} #read in table with opcodes
        self.table = self.load()
        self.stack = []
        self.localvar = [0]*10
        self.opcodes = opcodes
        self.class_ref = class_ref
        self.type = NONE

    def load(self):
        """Fills a dictionary with the bytecodes of different operational codes"""
        with open('jvpm/files/int_opcodes.csv', 'r') as csvfile:
            dict1 = {}
            spamreader = csv.DictReader(csvfile)
            for ind in list(spamreader):
                opcode_info = {'name': ind['name'].strip(), 
                    'num_initial_bytes': int(ind['num_initial_bytes'].strip()),
                    'type':int(ind['type'])}
                the_number = int(ind['opcode'].strip(), 16)
                dict1[the_number] = opcode_info
        return dict1

    def run(self):
        """"Runs method associated with opcode"""
        for opcode, value in self.opcodes:
            print("stack: ", self.stack)  # pragma: no cover
            print("running method: ",
                  self.table[opcode]['name'])  # pragma: no cover
            self.type = self.table[opcode]['type']
            if self.table[opcode]['num_arguments'] > 0:
                args = []
                for arg in value:
                    args.append(arg)
                getattr(self, self.table[opcode]['name'])(args)
            else:
                getattr(self, self.table[opcode]['name'])()
        return self.table[value]
        # test = input()

    def not_implemented(self):
        """Called when a certain element of the program is not yet implemented"""
        raise NotImplementedError("This function is not implemented.")

############################## PUSH TO STACK METHODS ###########################################
    def push_to_stack(self,val):
        if self.type == T_INT:
            self.push_int_to_stack(val)
        elif self.type == T_LONG:
            self.push_long_to_stack(val)
        elif self.type == T_FLOAT:
            self.push_float_to_stack(val)
        elif self.type == T_DOUBLE:
            self.stack.append(val)

    def pop_from_stack(self):
        if self.type == T_LONG:
            return self.pop_long_from_stack()
        elif self.type == T_INT:
            return self.stack.pop()
        elif self.type == T_FLOAT:
            return self.pop_float_from_stack()

    def push_int_to_stack(self, value):
        """Method to check if python is attempting to push a 64 bit integer which is
        not allowed in java"""
        if value > 2147483647 or value < -2147483648:
            raise ValueError()
        self.stack.append(value)

    def push_float_to_stack(self, value):
        """Method to check if python is attempting to push a 64 bit float which is
        not allowed in java"""
        if value > 2147483647 or value < -2147483648:
            raise ValueError()
        self.stack.append(numpy.float32(value))

    def pop_float_from_stack(self):
        """Method to check if python is attempting to push a 64 bit float which is
        not allowed in java"""
        value = self.stack.pop()
        if value > 2147483647 or value < -2147483648:
            raise ValueError("Invalid float")
        return numpy.float32(value)
    
    def push_long_to_stack(self, word):
        negative = 1
        if word > 2**63-1 or word < -(2**63):
            raise ValueError("long is too big or small")
        if word<0:
            negative = -1
            word*=-1
        self.stack.append(negative*self.extractLowerBits(word))
        self.stack.append(negative*self.extractUpperBits(word))
        
    def pop_long_from_stack(self):
        upperBits = self.stack.pop()
        lowerBits = self.stack.pop()
        negative = 1
        if upperBits<0 or lowerBits <0:
            negative = -1
        upperBits = abs(upperBits) << 32
        binaryWord = (abs(lowerBits) + upperBits)*negative
        return binaryWord

    def extractUpperBits(self, word):
        return (int(word) & 0xFFFFFFFF00000000) >> 32
		
    def extractLowerBits(self, word):
        return int(word) & 0x00000000FFFFFFFF
    
    ## start primitive type opcodes ##########################################################

    def add(self):
        """Adds two numbers in a stack and pushes the result back on"""
        self.push_to_stack(self.pop_from_stack() + self.pop_from_stack())

    def opcode_and(self):
        """Pushes the result of the operation 'and' of two numbers in the stack"""
        self.push_to_stack(self.pop_from_stack() & self.pop_from_stack())

    def const_m1(self):
        """Pushes '-1' onto the stack"""
        self.push_to_stack(-1)

    def const_0(self):
        """Pushes '0' unto the stack"""
        self.push_to_stack(0)

    def const_1(self):
        """pushes '1' unto the stack"""
        self.push_to_stack(1)

    def const_2(self):
        """Pushes '2' unto the stack"""
        self.push_to_stack(2)

    def const_3(self):
        """Pushes '3' unto the stack"""
        self.push_to_stack(3)

    def const_4(self):
        """Pushes '4' unto the stack"""
        self.push_to_stack(4)

    def const_5(self):
        """Pushes '5' unto the stack"""
        self.push_to_stack(5)

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
        self.push_to_stack(self.pop_from_stack()*self.pop_from_stack())

    def neg(self):
        """Pushes the next number in the stack multiplied by '-1'"""
        val = self.pop_from_stack() * (-1)
        print("neg",val)
        self.push_to_stack(val)

    def opcode_or(self):
        """Pushes the result of the operation 'or' of two numbers in the stack"""
        self.push_to_stack(self.pop_from_stack() | self.pop_from_stack())

    def rem(self):
        """Pushes the remainder of the second number in the stack divided by the next number"""
        self.push_to_stack(self.pop_from_stack() % self.pop_from_stack())

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
        self.push_to_stack(self.pop_from_stack()-self.pop_from_stack())

    def ushr(self):
        """Pushes the result of the second number in the stack with it's bytes shifted right
        arithmetically by the amount of the next number in the stack"""
        self.push_to_stack(
            (self.pop_from_stack() % 0x100000000) >> self.pop_from_stack())
        # needs testing

    def xor(self):
        """Pushes the result of the operation 'exclusive or' of two numbers in the stack"""
        self.push_to_stack(self.pop_from_stack() ^ self.pop_from_stack())

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

    def convert(self,to_type):
        val = self.pop_from_stack()
        self.type = to_type
        self.push_to_stack(val)

    def convert_double(self):
        self.convert(T_DOUBLE)
    
    def convert_int(self):
        self.convert(T_INT)

    def convert_long(self):
        self.convert(T_LONG)
    
    def convert_float(self):
        self.convert(T_FLOAT)

    def convert_byte(self):
        """Pushes the next number in the stack as a byte reference"""
        self.stack.append(self.pop_from_stack().to_bytes(
            length=1, byteorder='big', signed=True))

    def convert_char(self):
        """Pushes the next number in the stack as a character reference"""
        self.stack.append(chr(self.pop_from_stack()))

    def convert_short(self):
        op_max = 2**16-1
        op_min = -2**16
        m_number = 1.0
        value = self.pop_from_stack()
        if op_min <= value <= op_max:
            self.stack.append(value/m_number)
        else:
            raise ValueError("Value {} cannot be converted to short".format(value))

    def ldc(self, index):
        """Pushes constant index to stack"""
        self.push_to_stack(index[0])

    def invoke_virtual(self, methodRef):
        """Method for reading a java invoke virtual method and applying the correct method
        from python"""
        invoke = {"java/io/PrintStream.println:(I)V": "print_primitive", "java/io/PrintStream.println:(Z)V": "print_boolean",
                  "Method java/io/PrintStream.println:(D)V": "print_primitive", "java/io/PrintStream.println:(Ljava/lang/String;)V": "print_string",
                  "java/util/Scanner.nextString:()Ljava.lang/String": "input_string", "java/util/Scanner.nextInt:()I": "input_int",
                  "java/util/Scanner.nextDouble:()D": "input_double"}
        if methodRef in invoke:
            return (getattr(self, invoke[methodRef])())
        else:
            self.not_implemented()

    def printInt(self):
        return int(self.pop_from_stack())

    def print_boolean(self):
        num = self.pop_from_stack()
        if num == 1:
            return "true"
        elif num == 0:
            return "false"
        else:
            raise TypeError("Value coudn't be intterpretted as a boolean.")

    def print_primitive(self):
        val = self.pop_from_stack()
        print(val)
        return val
    
    def print_string(self):
        """Is called when invokedVirtual method is called to print a string"""
        return str(self.stack.pop())

    def input_string(self):
        return str(input())

    def input_int(self):
        return int(input())
    
    def input_double(self):
        """Takes input as a float/double"""
        m_number = 1.0
        return input() / m_number