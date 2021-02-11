from huffman_tree import Tree


codes = {}

f = open('text.txt')
num = [0] * 300

while True:
    c = f.read(1)
    if c:
        num[ord(c)] += 1
    else:
        break

print(num)

trees = []  # Нужно заменить на сет!!!

for i in range(len(num)):
    if num[i]:
        trees.append(Tree(summ=num[i], letter=chr(i)))

trees.sort(key=lambda tree: tree.sum)
print(trees)

while len(trees) > 1:
    trees.append(Tree(left=trees[0], right=trees[1]))
    trees = trees[2::]
    trees.sort(key=lambda tree: tree.sum)

tree = trees[0]
print(tree)

tree.count_codes('', codes)
print(codes)

f.close()
f = open('text.txt', 'r')

res = open('res.txt', 'wb')
while True:
    c = f.read(1)
    if c:
        for i in codes[c]:
            if i == '1':
                res.write(bytes(1))
            else:
                res.write(bytes(0))

    else:
        break




