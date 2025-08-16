numbers = []

with open('001 - 100/013.txt', 'r') as f:
    numbers = [int(line) for line in f.read().split('\n')]

sum = 0

for number in numbers:
    sum += number

print(str(sum)[:10])