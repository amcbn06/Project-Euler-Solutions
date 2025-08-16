max_palindrome = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        if str(a * b) == str(a * b)[::-1]:
            max_palindrome = max(max_palindrome, a * b)

print(max_palindrome)