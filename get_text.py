from separator import SEPARATOR
from huffman_tree import *


# f = open('res.txt', 'rb')
# c = f.read()

f = open('res.txt', 'r', encoding='CP866')
tree, ln, c = f.read().split(SEPARATOR)
ln = int(ln)

print(ln, tree, c)
c = c.encode('CP866')
print(c)

binary_string = "{:08b}".format(int(c.hex(), 16))

if len(binary_string) > ln:
    binary_string = binary_string[len(binary_string) - ln::]
else:
    binary_string = '0' * (ln - len(binary_string)) + binary_string

print(binary_string)
print('len =', len(binary_string))


tree = tree_from_str(list(tree))
print(tree.get_string())

print('RESULT TEXT:')
while binary_string:
    letter, binary_string = tree.get_letter(binary_string)
    print(letter, end='')
