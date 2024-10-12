import sys

input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
q = int(input())

ln, lm = 1, 1

for _ in range(q):
    x,y,d = map(int,input().split())
    if d == 1:
        ln = max(ln, x + 1)
        lm = m = y
    elif d == 2:
        n = min(n, x - 1)
        lm = m = y
    elif d == 3:
        ln = n = x
        m = min(m, y - 1)
    elif d == 4:
        ln = n = x
        lm = max(lm, y + 1)
    elif d == 5:
        ln = max(ln, x + 1)
        lm = max(lm, y + 1)
    elif d == 6:
        n = min(n, x - 1)
        lm = max(lm, y + 1)
    elif d == 7:
        ln = max(ln, x + 1)
        m = min(m, y - 1)
    elif d == 8:
        n = min(n, x - 1)
        m = min(m, y - 1)
    else:
        ln = n = x
        lm = m = y


print((n - ln + 1) * (m - lm + 1))

# 제출 번호 : 85113063, 메모리 : 31120, 시간 : 196