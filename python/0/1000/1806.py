import sys
input = lambda: sys.stdin.readline().rstrip()

n, s = map(int, input().split())
nli = tuple(map(int, input().split()))

a = 0
res = n+1

en = 0
now = 0

for st in range(n):
    while now < s and en < n:
        now += nli[en]
        en += 1
    
    if now >= s:
        res = min(res, en - st)

    now -= nli[st]

if res == n+1:
    res = 0

print(res)

# 제출 번호 : 101856362, 메모리 : 42292, 시간 : 116