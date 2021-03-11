from huffman_tree import Tree
from separator import SEPARATOR


def count_letters():
    global num

    f = open('text.txt')
    num = [0] * 30000

    while True:
        c = f.read(1)
        if c:
            num[ord(c)] += 1
        else:
            break

    f.close()

    print(num)


def make_tree():
    global codes, tree
    codes = {}
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


def write_tree(filename='res.txt', separator=SEPARATOR):
    res = open(filename, 'w')

    res.write(tree.get_string() + separator)

    res.close()


def write_bits():
    f = open('text.txt', 'r')

    bitstring = ''

    while True:
        c = f.read(1)
        if c:
            bitstring += codes[c]
        else:
            break

    print('all code: ', bitstring)
    print('len =', len(bitstring))

    res = open('tree.txt', 'a')
    res.write(f'{SEPARATOR}{len(bitstring)}')
    res.close()

    res = open('res.txt', 'wb')

    n = int(bitstring, 2)
    bytess = n.to_bytes((n.bit_length() + 7) // 8, 'big')
    print(bytess)

    res.write(bytess)

    res.close()


if __name__ == '__main__':
    # Clear file
    f = open('res.txt', 'w')
    f.close()

    count_letters()
    make_tree()
    write_tree(filename='tree.txt', separator='')
    write_bits()



