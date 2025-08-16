limit = 1000

count = [0] * (limit + 1)

for a in range(1, limit + 1):
    for b in range(1, limit + 1):
        c = int((a * a + b * b) ** 0.5)
        if a * a + b * b != c * c:
            continue
        if a + b + c > limit:
            continue
        count[a + b + c] += 1

print(count.index(max(count)))