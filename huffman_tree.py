class Tree:
    def __init__(self, summ=None, left=None, right=None, letter=None):
        self.left, self.right = left, right
        self.letter = letter
        if summ is None:
            self.sum = left.sum + right.sum
        else:
            self.sum = summ

    def get_letter(self, code):
        if self.letter:
            return self.letter
        if code[0] == 0:
            return self.left.get_letter(code[1::])
        return self.right.get_letter(code[1::])

    def count_codes(self, code, codes):
        if self.letter:
            codes[self.letter] = code
            print(self.letter, code)

        if self.left:
            self.left.count_codes(code + '0', codes)
        if self.right:
            self.right.count_codes(code + '1', codes)

    def __str__(self):
        return f'Tree: sum={self.sum}, letter={self.letter}'

    def __repr__(self):
        return f'<{self}>'
