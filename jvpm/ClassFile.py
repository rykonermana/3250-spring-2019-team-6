import unittest
import csv
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
            #self.cp_ic_fc_mc = self.cp_ic_fc + len(self.method_table)
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
    #     return self.data[12 + self.constant_pool_length] + self.data[13 + self.constant_pool_length]
    #
    # def get_super_class(self):
    #     return self.data[14 + self.constant_pool_length] + self.data[15 + self.constant_pool_length]
    #
    # def get_interface_count(self):
    #     return self.data[16 + self.constant_pool_length] + self.data[17 + self.constant_pool_length]
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

    #def get_method_count(self):
    #    return self.data[20 + self.cp_ic_fc] + self.data[21 + self.cp_ic_fc]

    #def get_method_table(self):
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
    #     print(self)
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
    #    print("Method count: ", self.method_count)
    #     print("Cp + IC + Fc + Mc: ", self.cp_ic_fc_mc)
    #    print("Opcode table: ",''.join("%02x, "%i for i in self.method_table))
    #     print("Attribute count: ", self.attribute_count)
    #     print("Attribute table: ", "[%s]" % ", ".join(map(str, self.attribute_table)))

    # def run_opcodes(self):
    #    opcodes = OpCodes(self.method_table)
    #    opcodes.run()

#
# if '__main__' == __name__:
#     ClassFile()

class OpCodes:
    def __init__(self,opcodes=[]):
        self.table = self.load() #{0x00: self.not_implemented} #read in table with opcodes
        self.stack = []
        self.opcodes = opcodes
        #self.run()

    def load(self):
	    dict1 = {}
	    with open('jvpm/files/int_opcodes.csv', 'r') as csvfile:
		    spamreader = csv.DictReader(csvfile)
		    for x in list(spamreader):
			    the_number = int(x['opcode'].strip(),16)
			    dict1[the_number]=x['name'].strip()
	    return dict1

    def run(self):
        for _ in self.opcodes:
            print("stack: ", self.stack)
            #method = self.interpret(i)
            #print("running method", method, "...")
            #print("finished method", method, "...")
            #test = input()

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        print("running method: ", self.table[value])
        getattr(self, self.table[value])()
        return self.table[value]

    def push_int_to_stack(self,value):
        if(value>2147483647 or value<-2147483648):
            raise ValueError()
        else:
            self.stack.append(value)

    #adds top two operands in the stack and returns the value
    def iadd(self):
        self.push_int_to_stack(self.stack.pop() + self.stack.pop())
		
    #Compares top two integer bits in the stack and returns the AND result
    def iand(self):
        self.push_int_to_stack(self.stack.pop() & self.stack.pop())

    #Pushes -1 onto the stack
    def iconst_m1(self):
        self.push_int_to_stack(-1)

    #Pushes 0 onto the stack
    def iconst_0(self):
        self.push_int_to_stack(0)

    #Pushes 1 onto the stack
    def iconst_1(self):
        self.push_int_to_stack(1)

    #Pushes 2 onto the stack
    def iconst_2(self):
        self.push_int_to_stack(2)

    #Pushes 3 onto the stack
    def iconst_3(self):
        self.push_int_to_stack(3)

    #Pushes 4 onto the stack
    def iconst_4(self):
        self.push_int_to_stack(4)

    #Pushes 5 onto the stack
    def iconst_5(self):
        self.push_int_to_stack(5)

    #Divides top two integers on the stack and pushes the integer answer
    def idiv(self):
        self.push_int_to_stack(self.stack.pop()//self.stack.pop())

    #Multiplies top two integers on the stack and pushes the result to the stack
    def imul(self):
        self.push_int_to_stack(self.stack.pop()*self.stack.pop())

    #Pushes the next integer on the stack *-1
    def ineg(self):
        self.push_int_to_stack(self.stack.pop() * (-1))

    #Pushes bitwise int OR into the stack of the top two integers
    def ior(self):
        self.push_int_to_stack(self.stack.pop()|self.stack.pop())

    #Pushes the remainder of the division of the top two integers in the stack
    def irem(self):
        self.push_int_to_stack(self.stack.pop()%self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was shifted left by the amount
    #of the the second integer on the stack
    def ishl(self):
        self.push_int_to_stack(self.stack.pop()<<self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was arithmetically shifted right by the amount
    #of the the second integer on the stack
    def ishr(self):
        self.push_int_to_stack(self.stack.pop()>>self.stack.pop())

    #Pushes the result of the top two integers of the stack back onto the stack
    def isub(self):
        self.push_int_to_stack(self.stack.pop()-self.stack.pop())

    #Pushes the next integer on the stack back onto it after it was logically shifted right by the amount
    #of the the second integer on the stack
    def iushr(self):
        self.push_int_to_stack((self.stack.pop() % 0x100000000) >> self.stack.pop())#needs testing

    #Pushes the exclusive OR result of the top two integers of the stack back onto the stack
    def ixor(self):
        self.push_int_to_stack(self.stack.pop() ^ self.stack.pop())