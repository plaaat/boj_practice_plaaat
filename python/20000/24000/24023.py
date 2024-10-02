import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = list(map(int, input().split()))
s, f = -1, -1
tn = 0
tf = False

for i in range(n):
    if (a[i] | k) != k:
        tn = 0
        s = -1
    else:
        if s == -1:
            s = i
        tn |= a[i]
        if tn == k:
            f = i
            tf = True
            break

if not tf:
    print(-1)
else:
    print(s + 1, f + 1)

# 제출 번호 : 84603259, 메모리 : 54132. 시간 : 148