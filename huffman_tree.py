def tree_from_str(s):
    if s[0] != '-':
        return Tree(byte=s.pop(0))

    s.pop(0)
    return Tree(left=tree_from_str(s), right=tree_from_str(s))


class Tree:
    def __init__(self, summ=None, left=None, right=None, byte=None):
        self.left, self.right = left, right
        self.byte = byte
        if summ is None:
            if self.left and self.right:
                self.sum = left.sum + right.sum
            else:
                self.sum = 0
        else:
            self.sum = summ

    def get_byte(self, code):
        if self.byte:
            return self.byte, code
        if code[0] == '0':
            return self.left.get_byte(code[1::])
        return self.right.get_byte(code[1::])

    def count_codes(self, code, codes):
        if self.byte:  # Не работает если в файле 1 символ!!!
            codes[self.byte] = code
            print(self.byte, code)

        if self.left:
            self.left.count_codes(code + '0', codes)
        if self.right:
            self.right.count_codes(code + '1', codes)

    def get_string(self):
        if self.byte:
            return 'b', self.byte

        l, r = self.left.get_string(), self.right.get_string()

        return f'-{l[0]}{r[0]}', l[1] + r[1]

    def __str__(self):
        return f'Tree: sum={self.sum}, byte={self.byte}'

    def __repr__(self):
        return f'<{self}>'
