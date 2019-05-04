def parse_bytes_value(bytes, start, length):
    """sums values of bytes of length 'length'
    """
    value = 0
    for i in range(length):
        value += bytes[start + i]
    return value
