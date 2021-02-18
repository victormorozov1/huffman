f = open('res.txt', 'rb')
c = f.read()
print(c)


binary_string = "{:08b}".format(int(c.hex(), 16))
print(binary_string)