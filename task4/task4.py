import sys

f_name = sys.argv[1]
ar = []

with open(f_name) as f:
    for elem in f:
        n = int(elem.strip())
        ar.append(n)

ar.sort()
ind1, ind2 = (len(ar) - 1) // 2, len(ar) // 2
moda = (ar[ind1] + ar[ind2]) // 2
res = sum(abs(elem - moda) for elem in ar)
print(res)
