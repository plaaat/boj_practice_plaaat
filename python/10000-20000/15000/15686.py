import sys
from itertools import combinations

input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
ho = []
ch = []

for i in range(n):
    li = list(map(int, input().split()))
    for s in range(n):
        if li[s] == 1:
            ho.append([i, s])
        elif li[s] == 2:
            ch.append([i, s])

pn = float('inf')
for i in combinations(ch, m):
    tem = 0
    for s in ho: 
        teml = float('inf')
        for j in range(m):
            teml = min(teml, abs(s[0] - i[j][0]) + abs(s[1] - i[j][1]))
        tem += teml
    pn = min(pn, tem)

print(pn)