import sys
import heapq

input = lambda:sys.stdin.readline().rstrip()
n,m = map(int,input().split())
s = int(input())
li = {}
num = [float('inf') for _ in range(n+1)]
num[s] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if a in li:
        li[a].append((b,c))
    else:
        li[a] = [(b,c)]

q = []
heapq.heappush(q,(0,s))
while q:
    co,di = heapq.heappop(q)
    if num[di] < co or not di in li:
        continue
    for i in li[di]:
        teco = co+i[1]
        if teco<num[i[0]]:
            heapq.heappush(q,(teco,i[0]))
            num[i[0]] = teco

for i in num[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)#  제출 번호 : 80938828, 메모리 : 69756, 시간 : 640