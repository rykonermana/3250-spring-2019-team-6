DIRECTORY = "" #""C:/Users/swanc/Documents/CS3250/temp/3250-spring-2019-team-6/"
NONE, T_INT, T_LONG, T_FLOAT, T_DOUBLE, T_OBJECT = 0, 1, 2, 3, 4, 5


def parse_bytes_value(bytes, start, length):
    """sums values of bytes of length 'length'
    """
    value = 0
    for i in range(length):
        value += bytes[start + i]
    return value
