words = open('001 - 100/042.txt', 'r').read().replace('"','').split(',')

def is_triangle(x):
    n = int((x * 2) ** 0.5)
    return n * (n + 1) // 2 == x

counter = 0

for word in words:
    sum = 0
    for character in word:
        sum += ord(character) - ord('A') + 1
    if is_triangle(sum):
        counter += 1

print(counter)