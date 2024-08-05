import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
dic = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a].append([c,b])

s,f = map(int,input().split())
q = []
q.append([0,s])
cost_list = [float('inf')]*(n+1)
cost_list[s] = 0
while q:
    cost,node = heapq.heappop(q)
    if node == f:
        print(cost)
        break
    if cost > cost_list[node]:
        continue
    for c,i in dic[node]:
        newc = cost+c
        if newc<cost_list[i]:
            cost_list[i] = newc
            heapq.heappush(q,[newc,i])
#  제출 번호 : 80100596, 메모리 : 60444, 시간 : 288