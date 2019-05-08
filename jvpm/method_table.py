"""Class to parse the Java bytecode constant pool"""
import csv


class MethodTable:
    """class to parse Java bytecode constant pool"""

    def __init__(self, data, count, init_position):
        """class to parse Java bytecode constant pool"""
        self.data = data
        self.method_pool_count = count
        self.init_position = init_position
        self.method_pool_helper = self.load_method_helper()
        self.method_table, self.final_byte = self.get_method_table()

    def get_method_table(self):
        """parses java byte code to retrieve raw constant pool"""
        the_table = {}
        active_position = self.init_position
        for i in range(1, self.method_pool_count+1):
            # 3 steps here: get constant type from bytes, get additional bytes for constant code,
            # get utf-8 variable length message. split???
            opcode = self.data[active_position:active_position+1]
            active_position += 1
            message_length = self.method_pool_helper[opcode]['num_initial_bytes']
            dict_constant = {'opcode': opcode,
                             'message': self.data[active_position:active_position+message_length]}
            active_position += message_length
            the_table[i] = dict_constant
        return the_table, (active_position - self.init_position)

    def load_method_helper(self):
        """Loads a dictionary to determine the method"""
        dict_variable_length = {}
        with open('jvpm/files/constant_codes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for constant in list(spamreader):
                method_info = {}
                method_info['num_initial_bytes'] = int(
                    constant['num_initial_bytes bytes'].strip())
                method_info['variable_length'] = False
                the_number = int(constant['opcode'].strip(), 16)
                dict_variable_length[the_number] = method_info
        return dict_variable_length
