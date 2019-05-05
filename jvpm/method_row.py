from jvpm.attribute import *
from jvpm.utils import *

METHOD_FLAGS_LENGTH = 2
METHOD_NAME_LENGTH = 2
METHOD_DESCRIPTOR_LENGTH = 2
METHOD_ATTRIBUTE_COUNT_START = METHOD_FLAGS_LENGTH + METHOD_NAME_LENGTH + METHOD_DESCRIPTOR_LENGTH
METHOD_ATTRIBUTE_COUNT_LENGTH = 2

ATTRIBUTE_CODE_LENGTH_START = 4
ATTRIBUTE_CODE_LENGTH_LENGTH = 4


class MethodRow:
    def __init__(self, data, start_position):
        self.data = data
        self.start_position = start_position
        self.name_index = parse_bytes_value(self.data, self.start_position + METHOD_FLAGS_LENGTH, METHOD_NAME_LENGTH)
        self.attribute_count = self.get_attribute_count()
        self.total_length = METHOD_ATTRIBUTE_COUNT_START + METHOD_ATTRIBUTE_COUNT_LENGTH
        self.attributes = self.get_attributes()

    def get_attribute_count(self):
        return parse_bytes_value(self.data, self.start_position+METHOD_ATTRIBUTE_COUNT_START,
                                 METHOD_ATTRIBUTE_COUNT_LENGTH)

    def get_attributes(self):
        attributes = []
        for _ in range(self.attribute_count):
            attribute = Attribute(self.data, self.start_position + self.total_length)
            self.total_length += attribute.total_length
            attributes.append(attribute)
        return attributes

    def get_op_code_bytes(self):
        attribute_bytes = self.attributes[0].get_attribute_bytes()
        op_code_bytes_length = parse_bytes_value(attribute_bytes, ATTRIBUTE_CODE_LENGTH_START,
                                                ATTRIBUTE_CODE_LENGTH_LENGTH)
        start = ATTRIBUTE_CODE_LENGTH_START + ATTRIBUTE_CODE_LENGTH_LENGTH
        return attribute_bytes[start:start+op_code_bytes_length]

    def __str__(self):
        return "{}\n{}: {}\n{}: {}\n{}".format("Method", "Name Index", self.name_index,
                                               "Attribute Count", self.attribute_count,
                                               "\n\n".join([str(a) for a in self.attributes]))
