import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())
r,c = map(int,input().split())

d = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
king = [(r,c)]

for dr,dc in d:
    dr += r
    dc += c
    if 1 <= dr <= n and 1 <= dc <= n:
        king.append((dr,dc))
visit = set()
for _ in range(k):
    rr,cc = map(int,input().split())
    for kr,kc in king:
        if abs(rr - kr) == abs(cc - kc) or rr == kr or cc == kc:
            visit.add((kr,kc))

if (r,c) in visit:
    print('CHECKMATE' if len(visit) == len(king) else 'CHECK')
else:
    print('STALEMATE' if len(visit) == len(king) - 1 else 'NONE')

# 제출번호 : 90260781, 메모리 : 32412, 시간 : 440
