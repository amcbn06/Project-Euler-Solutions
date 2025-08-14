grid = [[]]

with open(r'001 - 100\011\input.txt', 'r') as f:
    grid = [[int(x) for x in line.split()] for line in f.read().split('\n')]

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

max_product = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        for d in range(4):
            product = 1
            for i in range(4):
                nx = x + dx[d] * i
                ny = y + dy[d] * i
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    product *= grid[nx][ny]
                else:
                    product = 0
                    break
            if product > max_product:
                max_product = product

print(max_product)