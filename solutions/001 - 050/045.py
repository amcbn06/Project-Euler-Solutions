limit = 100000

T = set([ i * (i + 1) // 2 for i in range(1, limit)])
P = set([ i * (3 * i - 1) // 2 for i in range(1, limit)])
H = set([ i * (2 * i - 1) for i in range(1, limit)])

common = T.intersection(P).intersection(H)

print(list(common)[2])