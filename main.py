f = open('text.txt')
num = [0] * 300

while True:
    c = f.read(1)
    if c:
        num[ord(c)] += 1
    else:
        break

print(num)



