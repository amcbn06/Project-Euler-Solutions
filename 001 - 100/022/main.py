names = open('001 - 100/022/names.txt').read().replace('"', '').split(',')

names.sort()

total = 0

for index, name in enumerate(names):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    total += score * (index + 1)

print(total)