import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    nli = []
    res = 0
    for _ in range(n):
        nli.append(list(map(int,input().split())))
    coa = list(map(int,input().split()))

    for li in nli:
        t = float('inf')
        mon = li.pop()
        for s in li[1:]:
            t = min(t,coa[s-1])
        res += mon * t
    print(res)