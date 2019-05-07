"""This program runs a java virtual machine using python"""
from jvpm.constant_table import *
from jvpm.opcode_parser import *
from jvpm.method_row import *
from jvpm.OpCodes import *


class ClassFile:
    """Main file of the java python virtual machine"""
    def __init__(self, file=""):
        with open(file, 'rb') as binary_file:
            self.data = binary_file.read()
            self.magic = self.get_magic()
            self.minor = self.get_minor()
            self.major = self.get_major()
            self.constant_pool_count = self.get_constant_pool() - 1
            self.constant_table = ConstantTable(self.data, self.constant_pool_count)
            self.constant_pool_length = self.constant_table.final_byte
            # skipping access flags, class, super class
            self.interface_count = self.get_interface_count()
            assert self.interface_count == 0  # Interface table not implemented
            self.cp_and_ic = self.interface_count + self.constant_pool_length
            self.field_count = self.get_field_count()
            assert self.field_count == 0  # Field table parse not implemented
            self.cp_ic_fc = self.cp_and_ic + self.field_count
            self.method_count = self.get_method_count()
            assert self.method_count == 2  # not implemented for a java file with more than 1 method
            self.method_table = self.get_method_table()


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

    def get_interface_count(self):
        return self.data[16 + self.constant_pool_length] + self.data[17
            + self.constant_pool_length]

    def get_field_count(self):
        return self.data[18 + self.cp_and_ic] + self.data[19 + self.cp_and_ic]

    def get_method_count(self):
       return parse_bytes_value(self.data, 20 + self.cp_ic_fc, 2)

    def get_method_table(self):
        table = []
        start_length = self.cp_ic_fc +22
        for _ in range(self.method_count):
            row = MethodRow(self.data, start_length)
            start_length += row.total_length
            table.append(row)
        return table

    def __str__(self):
        """Prints out to the console"""
        result = "{} {}\n".format("Magic:", self.magic)
        result += "{} {}\n{} {}\n{} {}\n{}\n".format(
            "Minor version: ", self.minor,
            "Major version: ", self.major, "Constant pool count: ",
            self.constant_pool_count, str(self.constant_table))
        result += "{} {}\n{} {}\n{} {}\n{} {}\n{} {}\n{}{}".format(
            "Interface count: ", self.interface_count,
            "Cp + Ic: ", self.cp_and_ic, "Field count: ", self.field_count,
            "Cp + Ic + fc: ", self.cp_ic_fc, "Method count: ", self.method_count,
            "Method table: ", "\n".join(["\n" + str(a) for a in self.method_table]))
        return result

    def run_opcodes(self):
        """Runs the opcode class with the method table passed through it"""
        raw_op_code_bytes = self.method_table[1].get_op_code_bytes()
        formatted_op_code = OpcodeParse(raw_op_code_bytes).op_code_table
        opcodes = OpCodes(self, formatted_op_code)
        opcodes.run()

def main():
    classy = ClassFile(DIRECTORY + "jvpm/files/HelloWorld.class")
    classy.run_opcodes()
    #print(str(classy))


if __name__ == "__main__":
    # must call the main method
    main()

