import sys
import math
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
li = [list(map(int,input().split())) for _ in range(t)]
start = [0,0]

for x,y in li:
    start = [start[0]+x,start[1]+y]

print(*start)

mi = float('inf')
for i in range(t):
    start = [0,0]
    for s in range(t):
        if i == s:
            continue
        start = [start[0]+li[s][0],start[1]+li[s][1]]
    mi = min(mi,((start[0])**2+(start[1])**2)**0.5)

print('{:.2f}'.format(mi))

# 제출 번호 : 82411815,  메모리 : 33240,  시간 : 44