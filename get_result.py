from huffman_tree import *
from functions import read_bytes


END_FILE = 'res.jpg'


def get_tree_list():
    global tree_list

    tree_list = list(open('result/tree.txt', 'r').read())
    print(tree_list)
    for byte in read_bytes('result/tree_bytes.txt'):
        print(byte)
        tree_list[tree_list.index('b')] = byte
    print('Tree list =', tree_list)


def get_binary_string():
    global binary_string

    bits = open('result/res.txt', 'rb').read()

    binary_string = "{:08b}".format(int(bits.hex(), 16))

    if len(binary_string) > ln:
        binary_string = binary_string[len(binary_string) - ln::]
    else:
        binary_string = '0' * (ln - len(binary_string)) + binary_string


if __name__ == '__main__':
    get_tree_list()
    ln = int(open('result/len.txt', 'r').read())
    get_binary_string()

    tree = tree_from_str(list(tree_list))

    result = open(END_FILE, 'wb')
    while binary_string:
        byte, binary_string = tree.get_byte(binary_string)
        result.write(byte)

    print('Result is in', END_FILE)
