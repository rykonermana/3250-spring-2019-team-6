"""This program runs a java virtual machine using python"""
import unittest
import csv
import struct
import array
from constant_table import ConstantTable
# unittest


class ClassFile:
    """Main file of the java python virtual machine"""
    def __init__(self, file='test/HelloWorld.class'):
        with open(file, 'rb') as binary_file:
            # the byte string being stored in self.data to be parsed
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            self.constant_pool_count = self.get_constant_pool()-1
            self.constant_table = ConstantTable(self.data, self.constant_pool_count)
            self.constant_pool_length = self.constant_table.final_byte
            # self.access_flags = self.get_access_flags()
            # self.this_class = self.get_this_class()
            # self.superclass = self.get_super_class()
            # self.interface_count = self.get_interface_count()
            # self.cp_and_ic = self.interface_count + self.constant_table['length']
            # self.interface_table = self.get_interface_table()
            # self.field_count = self.get_field_count()
            self.cp_ic_fc = 224 #  = self.cp_and_ic + self.field_count
            # self.field_table = self.get_field_table()
            # self.method_count = self.get_method_count()
            # self.method_table = self.get_method_table()
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

    #
    # def get_access_flags(self):
    #     return self.data[10 + self.constant_pool_length-1:11 + self.constant_pool_length]
    #
    # def get_this_class(self):
    #     return self.data[12 + self.constant_pool_length]
    #     + self.data[13 + self.constant_pool_length]
    #
    # def get_super_class(self):
    #     return self.data[14 + self.constant_pool_length]
    #     + self.data[15 + self.constant_pool_length]
    #
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
    #
    # def get_field_table(self):
    #     field = self.data[self.cp_and_ic+20:(self.field_count+self.cp_ic_fc+20)]
    #     # for i in range(self.field_count):
    #     #    field += format(self.data[i + 20 + self.cp_and_ic], '02X')
    #     return field

    # def get_method_count(self):
    #    return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]

    # def get_method_table(self):
    #    method = self.data[22+self.cp_ic_fc:22+self.cp_ic_fc+self.method_count]
    #    return method
    #
    # def get_attribute_count(self):
    #     return self.data[22 + self.cp_ic_fc_mc] + self.data[23 + self.cp_ic_fc_mc]
    #
    # def get_attribute_table(self):
    #     attribute = self.data[(24+self.cp_ic_fc_mc):(24+self.cp_ic_fc_mc+self.attribute_count)]
    #     # for i in range(self.attribute_count):
    #     #    attribute += format(self.data[i + 24 + self.cp_ic_fc_mc], '02X')
    #     return attribute

    def print_self(self):
        """Prints out to the console"""
        print("Magic: ", self.magic)
        print("Minor version: ", self.minor)
        print("Major version: ", self.major)
        print("Constant pool count: ", self.constant_pool_count)
        self.constant_table.print_message()
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

    def run_opcodes(self):
        """Runs the opcode class with the method table passed through it"""
        opcodes = OpCodes(self.method_table)
        opcodes.run()

# if '__main__' == __name__:
#     ClassFile()


#   class LocalVar:
#   def __init__(self, localvar=[]):
#       self.localvar = localvar


class OpCodes:
    """This class defines a method for operational codes that java virtual machine uses"""
    def __init__(self, opcodes=[]):
        self.table = self.load()  # {0x00: self.not_implemented} #read in table with opcodes
        self.stack = []
        self.localvar = [0]*10
        self.opcodes = opcodes
        # self.run()

    def load(self):
        """Fills a dictionary with the bytecodes of different operational codes"""
        dict1 = {}
        with open('jvpm/files/int_opcodes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for ind in list(spamreader):
                the_number = int(ind['opcode'].strip(), 16)
                dict1[the_number] = ind['name'].strip()
        return dict1

    def run(self):
        """"Prints to the console a list of the opcodes"""
        for _ in self.opcodes:
            print("stack: ", self.stack)  # pragma: no cover
            # method = self.interpret(i)
            # print("running method", method, "...")
            # print("finished method", method, "...")
            # test = input()

    def not_implemented(self):
        """Called when a certain element of the program is not yet implemented"""
        return 'not implemented'

    def interpret(self, value):
        """Interprets"""
        print("running method: ", self.table[value])  # pragma: no cover
        getattr(self, self.table[value])()
        return self.table[value]

    def push_int_to_stack(self, value):
        """Method to check if python is attempting to push a 64 bit integer which is
        not allowed in java"""
        if value > 2147483647 or value < -2147483648:
            raise ValueError()
        self.stack.append(value)

    def iadd(self):
        """Adds the next two numbers in a stack and pushes the result back on"""
        self.push_int_to_stack(self.stack.pop() + self.stack.pop())

    def iand(self):
        """Pushes the result of the operation 'and' of two numbers in the stack"""
        self.push_int_to_stack(self.stack.pop() & self.stack.pop())

    def iconst_m1(self):
        """Pushes '-1' onto the stack"""
        self.push_int_to_stack(-1)

    def iconst_0(self):
        """Pushes '0' unto the stack"""
        self.push_int_to_stack(0)

    def iconst_1(self):
        """pushes '1' unto the stack"""
        self.push_int_to_stack(1)

    def iconst_2(self):
        """Pushes '2' unto the stack"""
        self.push_int_to_stack(2)

    def iconst_3(self):
        """Pushes '3' unto the stack"""
        self.push_int_to_stack(3)

    def iconst_4(self):
        """Pushes '4' unto the stack"""
        self.push_int_to_stack(4)

    def iconst_5(self):
        """Pushes '5' unto the stack"""
        self.push_int_to_stack(5)

    def idiv(self):
        """Pushes the result of the second number in the stack divided by the next
         number in the stack"""
        self.push_int_to_stack(self.stack.pop()//self.stack.pop())

    def imul(self):
        """Pushes the result of the top two numbers in the stack"""
        self.push_int_to_stack(self.stack.pop()*self.stack.pop())

    def ineg(self):
        """Pushes the next number in the stack multiplied by '-1'"""
        self.push_int_to_stack(self.stack.pop() * (-1))

    def ior(self):
        """Pushes the result of the operation 'or' of two numbers in the stack"""
        self.push_int_to_stack(self.stack.pop() | self.stack.pop())

    def irem(self):
        """Pushes the remainder of the second number in the stack divided by the next number"""
        self.push_int_to_stack(self.stack.pop() % self.stack.pop())

    def ishl(self):
        """Pushes the result of the second number in the stack with it's bytes shifted left
        by the amount of the next number in the stack"""
        self.push_int_to_stack(self.stack.pop() << self.stack.pop())

    def ishr(self):
        """Pushes the result of the second number in the stack with it's bytes shifted right
        by the amount of the next number in the stack"""
        self.push_int_to_stack(self.stack.pop() >> self.stack.pop())

    def isub(self):
        """Pushes the result of the second number in the stack minus the next number"""
        self.push_int_to_stack(self.stack.pop()-self.stack.pop())

    def iushr(self):
        """Pushes the result of the second number in the stack with it's bytes shifted right
        arithmetically by the amount of the next number in the stack"""
        self.push_int_to_stack((self.stack.pop() % 0x100000000) >> self.stack.pop())
        # needs testing

    def ixor(self):
        """Pushes the result of the operation 'exclusive or' of two numbers in the stack"""
        self.push_int_to_stack(self.stack.pop() ^ self.stack.pop())

    def iload(self, index):
        """Loads a variable from the variable array unto the stack"""
        self.stack.append(self.localvar[index])

    def iload_0(self, index):
        """Loads the variable of the variable array 'index 0' unto the stack"""
        self.stack.append(self.localvar[index])

    def iload_1(self, index):
        """Loads the variable of the variable array 'index 1' unto the stack"""
        self.stack.append(self.localvar[index])

    def iload_2(self, index):
        """Loads the variable of the variable array 'index 2' unto the stack"""
        self.stack.append(self.localvar[index])

    def iload_3(self, index):
        """Loads the variable of the variable array 'index 3' unto the stack"""
        self.stack.append(self.localvar[index])

    def istore(self, index):
        """Stores the next number in the stack onto the variable array on the given index"""
        self.localvar[index] = self.stack.pop()

    def istore_0(self, index):
        """Stores the next number in the stack onto the variable array on 'index 0'"""
        self.localvar[index] = self.stack.pop()

    def istore_1(self, index):
        """Stores the next number in the stack onto the variable array on 'index 1'"""
        self.localvar[index] = self.stack.pop()

    def istore_2(self, index):
        """Stores the next number in the stack onto the variable array on 'index 2'"""
        self.localvar[index] = self.stack.pop()

    def istore_3(self, index):
        """Stores the next number in the stack onto the variable array on 'index 3'"""
        self.localvar[index] = self.stack.pop()

    def i2b(self):
        """Pushes the next number in the stack as a byte reference"""
        self.stack.append(self.stack.pop().to_bytes(length=1, byteorder='big', signed=True))

    def i2c(self):
        """Pushes the next number in the stack as a character reference"""
        self.stack.append(chr(self.stack.pop()))

    def i2d(self):
        """Pushes the next number in the stack as a double reference"""
        self.stack.append(self.stack.pop()/1.0)

    def i2f(self):
        """Pushes the next number in the stack as a float reference"""
        self.stack.append(self.stack.pop()/1.0)

    def i2l(self):
        """Pushes the next number in the stack as a long reference"""
        op_max = 2 ** 64 - 1
        op_min = -2 ** 64
        value = self.stack.pop()
        if op_min <= value <= op_max:
            self.stack.append(value / 1.0)
        else:
            raise ValueError("Value {} cannot be converted to long".format(value))

    def i2s(self):
        """Pushes the next number in the stack as a short reference"""
        op_max = 2**16-1
        op_min = -2**16
        value = self.stack.pop()
        if op_min <= value <= op_max:
            self.stack.append(value/1.0)
        else:
            raise ValueError("Value {} cannot be converted to short".format(value))

    def invoke_virtual(self, methodRef):
        """Method for reading a java invoke virtual method and applying the correct method
        from python"""
        if methodRef == "java/io/PrintStream.println:(I)V":
            return int(self.stack.pop())
        # elif (methodRef == "java/util/Stack.push:(Ljava/lang/Object;)Ljava/lang/Object"):
        # return self.stack.append(self.stack.pop())
        elif methodRef == "java/io/PrintStream.println:(Z)V":
            num = self.stack.pop()
            if num == 1:
                return "true"
            elif num == 0:
                return "false"
            else:
                return "not a boolean"
                # Case probably raises an exception not 'not a boolean' - Christian
        # elif (methodRef == "Method java/io/PrintStream.println:(D)V"):
        #    return(long(self.stack.pop()))
        elif methodRef == "java/io/PrintStream.println:(Ljava/lang/String;)V":
            return self.stack.pop()
        elif methodRef == "java/util/Scanner.nextString:()Ljava.lang/String":
            return str(input())
        elif methodRef == "java/util/Scanner.nextInt:()I":
            return int(input())
        elif methodRef == "java/util/Scanner.nextDouble:()D":
            return float(input())
        else:
            return "not implemented"
