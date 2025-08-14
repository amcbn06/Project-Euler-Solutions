n = 10

used = [False] * n
permutation = []
index = 0

def backtracking():
    if len(permutation) == n:
        global index
        index += 1
        if index == 1000000:
            print(''.join([str(x) for x in permutation]))
            exit(0)

    for i in range(n):
        if not used[i]:
            used[i] = True
            permutation.append(i)
            backtracking()
            used[i] = False
            permutation.pop()


backtracking()