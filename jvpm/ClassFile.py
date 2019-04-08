import unittest
import csv
import struct
import array
from jvpm.constant_table import ConstantTable
# unittest


class ClassFile:
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
            # self.cp_ic_fc = 224 #  = self.cp_and_ic + self.field_count
            # self.field_table = self.get_field_table()
            # self.method_count = self.get_method_count()
            # self.method_table = self.get_method_table()
            # self.cp_ic_fc_mc = self.cp_ic_fc + len(self.method_table)
            # self.attribute_count = self.get_attribute_count()
            # self.attribute_table = self.get_attribute_table()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

    def get_constant_pool(self):
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
        opcodes = OpCodes(self.method_table)
        opcodes.run()

# if '__main__' == __name__:
#     ClassFile()


'''class LocalVar:
    def __init__(self, localvar=[]):
        self.localvar = localvar
'''


class OpCodes:

    def __init__(self, opcodes=[]):
        self.table = self.load() # {0x00: self.not_implemented} #read in table with opcodes
        self.stack = []
        self.localvar = [0]*10
        self.opcodes = opcodes
        # self.run()

    def load(self):
        dict1 = {}
        with open('jvpm/files/int_opcodes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for x in list(spamreader):
                the_number = int(x['opcode'].strip(), 16)
                dict1[the_number] = x['name'].strip()
        return dict1

    def run(self):
        for _ in self.opcodes:
            print("stack: ", self.stack)  # pragma: no cover
            # method = self.interpret(i)
            # print("running method", method, "...")
            # print("finished method", method, "...")
            # test = input()

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        print("running method: ", self.table[value])  # pragma: no cover
        getattr(self, self.table[value])()
        return self.table[value]

    def push_int_to_stack(self, value):
        if value>2147483647 or value < -2147483648:
            raise ValueError()
        else:
            self.stack.append(value)

    def iadd(self):
        self.push_int_to_stack(self.stack.pop() + self.stack.pop())

    def iand(self):
        self.push_int_to_stack(self.stack.pop() & self.stack.pop())

    def iconst_m1(self):
        self.push_int_to_stack(-1)

    def iconst_0(self):
        self.push_int_to_stack(0)

    def iconst_1(self):
        self.push_int_to_stack(1)

    def iconst_2(self):
        self.push_int_to_stack(2)

    def iconst_3(self):
        self.push_int_to_stack(3)

    def iconst_4(self):
        self.push_int_to_stack(4)

    def iconst_5(self):
        self.push_int_to_stack(5)

    def idiv(self):
        self.push_int_to_stack(self.stack.pop()//self.stack.pop())

    def imul(self):
        self.push_int_to_stack(self.stack.pop()*self.stack.pop())

    def ineg(self):
        self.push_int_to_stack(self.stack.pop() * (-1))

    def ior(self):
        self.push_int_to_stack(self.stack.pop() | self.stack.pop())

    def irem(self):
        self.push_int_to_stack(self.stack.pop() % self.stack.pop())

    def ishl(self):
        self.push_int_to_stack(self.stack.pop() << self.stack.pop())

    def ishr(self):
        self.push_int_to_stack(self.stack.pop() >> self.stack.pop())

    def isub(self):
        self.push_int_to_stack(self.stack.pop()-self.stack.pop())

    def iushr(self):
        self.push_int_to_stack((self.stack.pop() % 0x100000000) >> self.stack.pop())  # needs testing

    def ixor(self):
        self.push_int_to_stack(self.stack.pop() ^ self.stack.pop())

    def iload(self, index):
        self.stack.append(self.localvar[index])

    def iload_0(self, index):
        self.stack.append(self.localvar[index])

    def iload_1(self, index):
        self.stack.append(self.localvar[index])

    def iload_2(self, index):
        self.stack.append(self.localvar[index])

    def iload_3(self, index):
        self.stack.append(self.localvar[index])

    def istore(self, index):
        self.localvar[index] = self.stack.pop()

    def istore_0(self, index):
        self.localvar[index] = self.stack.pop()

    def istore_1(self, index):
        self.localvar[index] = self.stack.pop()

    def istore_2(self, index):
        self.localvar[index] = self.stack.pop()

    def istore_3(self, index):
        self.localvar[index] = self.stack.pop()

    def i2b(self):
        self.stack.append(self.stack.pop().to_bytes(length=1, byteorder='big', signed=True))

    def i2c(self):
        self.stack.append(chr(self.stack.pop()))

    def i2d(self):
        self.stack.append(self.stack.pop()/1.0)

    def i2f(self):
        self.stack.append(self.stack.pop()/1.0)

    def i2l(self):
        max = 2 ** 64 - 1
        min = -2 ** 64
        value = self.stack.pop()
        if min <= value <= max:
            self.stack.append(value / 1.0)
        else:
            raise ValueError("Value {} cannot be converted to long".format(value))

    def i2s(self):
        max = 2**16-1
        min = -2**16
        value = self.stack.pop()
        if min <= value <= max:
            self.stack.append(value/1.0)
        else:
            raise ValueError("Value {} cannot be converted to short".format(value))

    def invoke_virtual(self, method_Ref):
        if methodRef == "java/io/PrintStream.println:(I)V":
            return int(self.stack.pop())
        # elif (methodRef == "java/util/Stack.push:(Ljava/lang/Object;)Ljava/lang/Object"):
        # return self.stack.append(self.stack.pop())
        elif methodRef == "java/io/PrintStream.println:(Z)V":
            x = self.stack.pop()
            if x == 1:
                return "true"
            elif x == 0:
                return "false"
            else:
                return "not a boolean"  # Case probably raises an exception not 'not a boolean' - Christian
        # elif (methodRef == "Method java/io/PrintStream.println:(D)V"):
        #    return(long(self.stack.pop()))
        elif methodRef == "java/io/PrintStream.println:(Ljava/lang/String;)V":
            return self.stack.pop()
        elif methodRef == "java/util/Scanner.nextString:()Ljava.lang/String":
            return input()
        elif methodRef == "java/util/Scanner.nextInt:()I":
            return int(input())
        elif methodRef == "java/util/Scanner.nextDouble:()D":
            return double(input())
        else:
            return "not implemented"
