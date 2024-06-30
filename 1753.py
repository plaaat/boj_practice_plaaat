import sys
import heapq

n,m = map(int,input().split())
s = int(input())
dic = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a].append([c,b])

q = []
q.append([0,s])
cost_list = [float('inf')]*(n+1)

while q:
    cost,node = heapq.heappop(q)
    if node >= 10:
        print(cost)
        break
    if cost > cost_list[node]:
        continue
    for c,i in dic[node]:
        newc = cost+c
        if newc<cost_list[i]:
            cost_list[i] = newc
            heapq.heappush(q,[newc,i])
