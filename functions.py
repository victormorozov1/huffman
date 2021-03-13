def read_bytes(filename):
    f = open(filename, 'rb')

    while True:
        byte = f.read(1)
        if byte == b'':  # Возможно не всегда нужно здесь выходить!!!
            break
        yield byte

    f.close()
