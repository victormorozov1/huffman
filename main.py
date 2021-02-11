from huffman_tree import Tree


f = open('text.txt')
num = [0] * 300

while True:
    c = f.read(1)
    if c:
        num[ord(c)] += 1
    else:
        break

print(num)

trees = []

for i in range(len(num)):
    trees.append(Tree(num[i], letter=chr(i)))
    if num[i]:
        print(chr(i))

