import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

nli = [int(input()) for _ in range(m)]

nli.sort()
ma = -1
res = 0
for i in nli:
    t = 0
    tn = 0
    for j in nli:
        if tn == n:
            break
        if i <= j:
            t += i
            tn += 1
    if t > ma:
        ma = t
        res = i
print(res,ma)

# 제출번호 : 924999526, 메모리 : 32412, 시간 : 176