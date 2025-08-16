limit = 100000

answer = 0

for i in range(1, limit):
    concat = ""
    n = 1
    while len(concat) < 9:
        concat += str(i * n)
        n += 1
    if ''.join(sorted(concat)) != "123456789":
        continue
    print(i, concat)
    answer = max(answer, int(concat))

print(answer)