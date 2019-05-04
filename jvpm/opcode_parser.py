import csv


class OpcodeParse:
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
            opcode = self.data[active_position]
            print(opcode)
            active_position += 1
            message_length = self.method_pool_helper[opcode]['num_initial_bytes']
            dict_constant = {'opcode': opcode,
                             'message': self.data[active_position:active_position+message_length]}
            active_position += message_length
            the_table[i] = dict_constant
        return the_table, (active_position - self.init_position)
    
    def load_method_helper(self):
        dict_variable_length = {}
        with open('C:/Users/swanc/Documents/CS3250/temp/3250-spring-2019-team-6/jvpm/files/int_opcodes.csv', 'r') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for constant in list(spamreader):
                print(constant)
                method_info = {'num_initial_bytes': int(
                    constant['num_initial_bytes'].strip())}
                method_info['variable_length'] = False
                the_number = int(constant['opcode'].strip(), 16)
                dict_variable_length[the_number] = method_info
        print(dict_variable_length)
        return dict_variable_length
