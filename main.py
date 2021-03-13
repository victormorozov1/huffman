from huffman_tree import Tree
from separator import SEPARATOR


def count_letters():
    global num

    f = open('text.txt', 'rb')
    num = {}

    while True:
        byte = f.read(1)
        if byte == b'':  # Возможно не всегда нужно здесь выходить!!!
            break
        print('byte =', byte, type(byte))
        if byte in num:
            num[byte] += 1
        else:
            num[byte] = 1

    f.close()

    print(num)


def make_tree():
    global codes, tree
    codes = {}
    trees = []  # Нужно заменить на сет!!!

    for byte, summ in sorted(num.items()):
        trees.append(Tree(summ=summ, letter=byte))

    trees.sort(key=lambda tree: tree.sum)
    print(trees)

    while len(trees) > 1:
        trees.append(Tree(left=trees[0], right=trees[1]))
        trees = trees[2::]
        trees.sort(key=lambda tree: tree.sum)

    tree = trees[0]
    print('Tree: ', tree)

    tree.count_codes('', codes)
    print('Codes: ', codes)


def write_tree():
    tree_file = open('tree.txt', 'w')
    bytes_file = open('tree_bytes.txt', 'wb')

    tree_str, tree_bytes = tree.get_string()

    tree_file.write(tree_str)
    bytes_file.write(tree_bytes)

    tree_file.close()
    bytes_file.close()


def write_bits():
    f = open('text.txt', 'rb')

    bitstring = ''

    while True:
        c = f.read(1)
        if c:
            bitstring += codes[c]
        else:
            break

    print('all code: ', bitstring)
    print('len =', len(bitstring))

    len_file = open('len.txt', 'w')
    len_file.write(str(len(bitstring)))
    len_file.close()

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
    write_tree()
    write_bits()



