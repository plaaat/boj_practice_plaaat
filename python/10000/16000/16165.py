import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
gg = {}
gm = {}

for _ in range(n):
    gn = input()
    t = int(input())
    gg[gn] = []
    for _ in range(t):
        gmn = input()
        gg[gn].append(gmn)
        gm[gmn] = gn

for _ in range(m):
    wo = input()
    ty = int(input())
    if ty:
        print(gm[wo])
    else:
        res = gg[wo]
        res.sort()
        print(*res, sep='\n')

# 제출 번호 : 96340500, 메모리 : 32412, 시간 : 44