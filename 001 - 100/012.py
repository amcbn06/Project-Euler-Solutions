def num_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:  # Count the complementary divisor only if it's different
                count += 1
    return count

i = 1

while num_divisors(i * (i + 1) // 2) <= 500:
    i += 1

print(i * (i + 1) // 2)