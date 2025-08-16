limit = 1000000

def palindromic(s):
    return s == s[::-1]

sum = 0

for i in range(1, limit):
    if palindromic(str(i)) and palindromic(bin(i)[2:]):
        sum += i

print(sum)