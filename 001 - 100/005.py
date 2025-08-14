def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

answer = 1
for i in range(1, 21):
    answer = lcm(answer, i)

print(answer)