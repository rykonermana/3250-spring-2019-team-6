import csv

INIT_POSITION = 10

class ConstantTable:
    """class to parse Java bytecode constant pool"""

    def __init__(self, data, count):
        """class to parse Java bytecode constant pool"""
        self.data = data
        self.constant_pool_count = count
        self.constant_pool_helper = load_constant_helper()
        self.constant_table, self.final_byte = self.get_constant_pool_table()
        self.get_constant_messages()

    def get_constant_pool_table(self):
        """parses java byte code to retrieve raw constant pool"""
        the_table = {}
        active_position = INIT_POSITION
        for i in range(1, self.constant_pool_count+1):
            # 3 steps here: get constant type from bytes, get additional bytes for constant code, get utf-8 variable length message. split???
            constant_code = self.parse_double_bytes_value(
                self.data, active_position)
            active_position += 1
            message_length = self.constant_pool_helper[constant_code]['num_initial_bytes']
            dict_constant = {'constant_code': constant_code,
                             'message': self.data[active_position:active_position+message_length]}
            active_position += message_length
            if self.constant_pool_helper[constant_code]['variable_length']:
                value_length = self.parse_double_bytes_value(
                    dict_constant['message'], 0)
                dict_constant['decrypted_message'] = self.data[active_position:
                                                               active_position+value_length].decode('utf-8', 'replace')
                active_position += value_length
            the_table[i] = dict_constant
        return the_table, (active_position - INIT_POSITION)

    def get_constant_messages(self):
        """loop through constants to get values"""
        for i in range(1, self.constant_pool_count+1):
            self.check_or_parse_constant(i)

    def check_or_parse_constant(self, constant_number):
        """check if final constant value exists or begin call to retrieve"""
        if not 'decrypted_message' in self.constant_table[constant_number].keys():
            parse_message_string = self.constant_pool_helper[
                self.constant_table[constant_number]['constant_code']]['decode']
            decoded = getattr(self, parse_message_string)(constant_number)
            self.constant_table[constant_number]['decrypted_message'] = decoded

    def nested_constant(self, number):
        """return all constants associated with something"""
        constant_code = self.constant_table[number]['constant_code']
        num_bytes = self.constant_pool_helper[constant_code]['num_initial_bytes']
        num_constants = num_bytes // 2  # 2 bytes per constant
        offset = num_bytes % 2  # Method handle first byte is some descriptor
        string_format = self.constant_pool_helper[constant_code]['format']
        constant_message = []
        for i in range(num_constants):
            constant_numbers = self.parse_double_bytes_value(
                self.constant_table[number]['message'], offset+2*i)
            self.check_or_parse_constant(constant_numbers)
            constant_message.append(
                self.constant_table[constant_numbers]['decrypted_message'])
        return str(string_format).join(constant_message)

    def parse_double_bytes_value(self, bytes, start):
        """returns values of two byte constant"""
        return bytes[start] + bytes[start+1]

    def __str__(self):
        """Return the javap version of the constant"""
        the_format = "{: >10} = {: <15}{}"
        the_result = "Constant pool: \n", "%s" % "\n ".join(map(lambda x: the_format.format('#'+str(x), self.constant_pool_helper[self.constant_table[x]['constant_code']]['description'],
                                                                                                       self.constant_table[x]['decrypted_message']), self.constant_table))
        return ''.join(the_result)


def load_constant_helper():
    """loads file with details on each constant type"""
    dict_variable_length = {}
    with open('jvpm/files/constant_codes.csv', 'r') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for constant in list(spamreader):
            constant_info = {}
            constant_info['num_initial_bytes'] = int(
                constant['Additional bytes'].strip())
            constant_info['variable_length'] = bool(
                int(constant['Variable Length'].strip()))
            constant_info['decode'] = constant['Decode']
            constant_info['format'] = constant['Constant Format']
            constant_info['description'] = constant['Description'].strip()
            the_number = int(constant['Tag byte'].strip(), 10)
            dict_variable_length[the_number] = constant_info
    return dict_variable_length
