import csv

class ConstantTable:
    """class to parse Java bytecode constant pool"""

    def __init__(self, data, count):
        """class to parse Java bytecode constant pool"""
        self.data = data
        self.constant_pool_count = count
        self.constant_pool_helper = load_constant_helper()
        self.constant_table, self.final_byte = self.get_constant_pool_table()
        print(self.constant_table)
        self.get_constant_messages()

    def get_constant_pool_table(self):
        """parses java byte code to retrieve raw constant pool"""
        the_table = {}
        active_position = 10
        for i in range(1, self.constant_pool_count+1):
            dict_constant = {}
            constant_code = 0
            for j in self.data[active_position:active_position+1]:
                constant_code += j
            active_position += 1
            dict_constant['constant_code'] = constant_code
            message_length = int(self.constant_pool_helper[constant_code]['num_initial_bytes'])
            dict_constant['message'] = self.data[active_position:active_position+message_length]
            dict_constant['decode'] = self.constant_pool_helper[constant_code]['decode']
            dict_constant['format'] = self.constant_pool_helper[constant_code]['format']
            active_position += message_length
            if self.constant_pool_helper[constant_code]['variable_length']:
                value_length = int(dict_constant['message'][0]) + int(dict_constant['message'][1])
                dict_constant['value'] = self.data[active_position:active_position+value_length]
                active_position += value_length
            the_table[i] = dict_constant
        return the_table, (active_position - 10)

    def get_constant_messages(self):
        """loop through constants to get values"""
        for i in range(1, self.constant_pool_count+1):
            self.check_or_parse_constant(i)

    def final_constant(self, number):
        """return constant for utf-8 constant"""
        return self.constant_table[number]['value'].decode('utf-8', 'replace')

    def check_or_parse_constant(self, constant_number):
        """check if final constant value exists or begin call to retrieve"""
        if not 'decrypted_message' in self.constant_table[constant_number].keys():
            decoded = getattr(self, self.constant_table[constant_number]['decode'])(constant_number)
            self.constant_table[constant_number]['decrypted_message'] = decoded

    def nested_constant_1(self, number):
        """return the final constant value for 1-byte code"""
        constant_number = self.constant_table[number]['message'][0]
        constant_number += self.constant_table[number]['message'][1]
        self.check_or_parse_constant(constant_number)
        return self.constant_table[constant_number]['decrypted_message']

    def nested_constant_2(self, number):
        """return the final constant value for 2-byte code"""
        constant_number_1 = self.constant_table[number]['message'][0]
        constant_number_1 += self.constant_table[number]['message'][1]
        constant_number_2 = self.constant_table[number]['message'][2]
        constant_number_2 += self.constant_table[number]['message'][3]
        self.check_or_parse_constant(constant_number_1)
        self.check_or_parse_constant(constant_number_2)
        return self.constant_table[number]['format'].format(self.constant_table[constant_number_1]['decrypted_message'], self.constant_table[constant_number_2]['decrypted_message'])

    def nested_constant_plus(self, number):
        """return the final constant value for a MethodHandle"""
        constant_number_1 = self.constant_table[number]['message'][1] + self.constant_table[number]['message'][2]
        self.check_or_parse_constant(constant_number_1)
        return self.constant_table[number]['format'].format(self.constant_table[constant_number_1])

    def print_message(self):
        """Return the javap version of the constant"""
        print("Constant pool: \n", "%s" % "\n ".join(map(lambda x: "{: >10} = {: <15}{}".format('#'+str(x), self.constant_pool_helper[self.constant_table[x]['constant_code']]['description'], self.constant_table[x]['decrypted_message']), self.constant_table)))

def load_constant_helper():
    """loads file with details on each constant type"""
    dict_variable_length = {}
    with open('jvpm/files/constant_codes.csv', 'r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for constant in list(spamreader):
            constant_info = {}
            constant_info['num_initial_bytes'] = int(constant['Additional bytes'].strip())
            constant_info['variable_length'] = bool(int(constant['Variable Length'].strip()))
            constant_info['decode'] = constant['Decode']
            constant_info['format'] = constant['Constant Format']
            constant_info['description'] = constant['Description'].strip()
            the_number = int(constant['Tag byte'].strip(), 10)
            dict_variable_length[the_number] = constant_info
    return dict_variable_length
