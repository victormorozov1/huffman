from separator import SEPARATOR


# f = open('res.txt', 'rb')
# c = f.read()

f = open('res.txt', 'r', encoding='CP866')
tree, ln, *c = f.read().split(SEPARATOR)
ln = int(ln)
print(ln, tree, c)
c = c.encode('CP866')
print(c)

binary_string = "{:08b}".format(int(c.hex(), 16))
binary_string = binary_string[len(binary_string) - ln::]

print(binary_string)
print('len =', len(binary_string))
