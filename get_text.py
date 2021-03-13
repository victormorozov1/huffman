from separator import SEPARATOR
from huffman_tree import *
from functions import read_bytes


# f = open('res.txt', 'rb')
# c = f.read()

END_FILE = 'res.jpeg'


tree_list = list(open('tree.txt', 'r').read())
print(tree_list)
for byte in read_bytes('tree_bytes.txt'):
    print(byte)
    tree_list[tree_list.index('b')] = byte
print('Tree list =', tree_list)

ln = int(open('len.txt', 'r').read())

bits = open('res.txt', 'rb').read()

print(ln, tree_list, bits)

binary_string = "{:08b}".format(int(bits.hex(), 16))

if len(binary_string) > ln:
    binary_string = binary_string[len(binary_string) - ln::]
else:
    binary_string = '0' * (ln - len(binary_string)) + binary_string

print(binary_string)
print('len =', len(binary_string))


tree = tree_from_str(list(tree_list))
print(tree.get_string())

result = open(END_FILE, 'wb')

print('RESULT TEXT:')
while binary_string:
    letter, binary_string = tree.get_letter(binary_string)
    print(letter, end='')
    result.write(letter)
