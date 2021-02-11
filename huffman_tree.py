class Tree:
    def __init__(self, sum, left=None, right=None, letter=None):
        self.left, self.right = left, right
        self.letter = letter
        self.sum = sum

    def get_letter(self, code):
        if self.letter:
            return self.letter
        if code[0] == 0:
            return self.left.get_letter(code[1::])
        return self.right.get_letter(code[1::])
