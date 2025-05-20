import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
res = 1
now = 0

if n % 2 == 1:
    n1 = n // 2 + 1
    n2 = n // 2
else:
    n1, n2 = n // 2, n // 2
n3 = (n-1) // 3 + 1

if n == 1:
    if m == 0:
        print(1)
    else:
        print(2)
elif n == 2:
    if m == 0:
        print(1)
    elif m == 1:
        print(3)
    else:
        print(4)
else:
    if n1 <= m:
        res += 1
    if n2 <= m:
        res += 1
    if n <= m:
        res += 1

    if n3 <= m:
        res += 1
    if n1 + n3 <= m:
        res += 1
    if n2 + n3 <= m:
        res += 1
    if n + n3 <= m:
        res += 1
    print(res)

# 제출 번호 : 94557437, 메모리 : 32412, 시간 : 32