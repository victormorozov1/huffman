def tree_from_str(s):
    if s[0] != '-':
        return Tree(letter=s.pop(0))

    s.pop(0)
    return Tree(left=tree_from_str(s), right=tree_from_str(s))


class Tree:
    def __init__(self, summ=None, left=None, right=None, letter=None):
        self.left, self.right = left, right
        self.letter = letter
        if summ is None:
            if self.left and self.right:
                self.sum = left.sum + right.sum
            else:
                self.sum = 0
        else:
            self.sum = summ

    def get_letter(self, code):
        if self.letter:
            return self.letter, code
        if code[0] == '0':
            return self.left.get_letter(code[1::])
        return self.right.get_letter(code[1::])

    def count_codes(self, code, codes):
        if self.letter:  # Не работает если в файле 1 символ!!!
            codes[self.letter] = code
            print(self.letter, code)

        if self.left:
            self.left.count_codes(code + '0', codes)
        if self.right:
            self.right.count_codes(code + '1', codes)

    def get_string(self):
        if self.letter:
            return self.letter

        return '-' + self.left.get_string() + self.right.get_string()

    def __str__(self):
        return f'Tree: sum={self.sum}, letter={self.letter}'

    def __repr__(self):
        return f'<{self}>'


if __name__ == '__main__':
    s = ['-', 'a', '-', 'b', 'c']
    t = tree_from_str(s)
    print(t.get_string())
    print(t.left.get_letter('1011'))
    print(t.get_letter('01011'))

    code = '01011'
    while code:
        letter, code = t.get_letter(code)
        print(letter, code)