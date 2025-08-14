n = 7

used = [False] * (n + 1)
number = 0

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def backtracking():
    global number
    if len(str(number)) == n:
        if is_prime(number):
            print(number)
            exit(0)

    for i in range(n, 0, -1):
        if not used[i]:
            used[i] = True
            number = number * 10 + i
            backtracking()
            used[i] = False
            number = number // 10


backtracking()