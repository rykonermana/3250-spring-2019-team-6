"""class to parse Java bytecode constant pool"""
import csv
from jvpm.utils import DIRECTORY


class OpcodeParse:
    """class to parse Java bytecode constant pool"""

    def __init__(self, data, init_position=0):
        """class to parse Java bytecode constant pool"""
        self.data = data
        self.init_position = init_position
        self.method_pool_helper = self.load_method_helper()
        self.op_code_table = self.parse_op_codes()

    def parse_op_codes(self):
        """parses java byte code to retrieve raw constant pool"""
        the_table = []
        active_position = 0
        while active_position < len(self.data):
            op_code = self.data[active_position]
            active_position += 1
            message_length = self.method_pool_helper[op_code]['num_initial_bytes']
            dict_constant = {'opcode': op_code,
                             'message': self.data[active_position:active_position+message_length]}
            active_position += message_length
            the_table.append(dict_constant)
        return the_table
    
    def load_method_helper(self):
        """Returns the dictionary's variable length"""
        dict_variable_length = {}
        with open(DIRECTORY + 'jvpm/files/int_opcodes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for constant in list(spamreader):
                method_info = {'num_initial_bytes': int(constant['num_initial_bytes'].strip())}
                method_info['variable_length'] = False
                the_number = int(constant['opcode'].strip(), 16)
                dict_variable_length[the_number] = method_info
        return dict_variable_length
