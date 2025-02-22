import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
peo = [set() for _ in range(n+1)]
e = int(input())
song = 0

for _ in range(e):
    k = list(map(int,input().split()))
    ts = set()

    if 1 in k[1:]:
        song += 1
        for i in k[1:]:
            peo[i].add(song)
    else:
        for i in k[1:]:
            ts.update(peo[i])
        for i in k[1:]:
            peo[i] = ts.copy()

sorpeo = sorted(peo,key=lambda x: len(x))
maxn = len(sorpeo[-1])

for i in range(1,n+1):
    if len(peo[i]) == maxn:
        print(i)

# 제출번호 : 90350343, 메모리 : 32412, 시간 : 36