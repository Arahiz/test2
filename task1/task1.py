import sys

n, m = int(sys.argv[1]), int(sys.argv[2])
# n, m  = map(int, input().split())
i = 1
while True:
    print(i, end='')
    i = (i + m - 1) % n or n
    if i == 1:
        break
print()