import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nodes = [(tuple(map(int,input().split())),i) for i in range(n)]
graph = []

for i in range(3):
    nodes.sort(key=lambda x: x[0][i])
    for j in range(n-1):
        graph.append((abs(nodes[j][0][i] - nodes[j+1][0][i]),nodes[j][1],nodes[j+1][1]))

graph.sort()
par = [i for i in range(n)]

def find_p(p,x):
    if p[x] != x:
        p[x] = find_p(p,p[x])
    return p[x]

def uni(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

res = 0
for c,a,b in graph:
    if find_p(par,a) != find_p(par,b):
        uni(par,a,b)
        res += c
    
print(res)

# 제출 번호: 102631146, 메모리 : 94560, 시간 : 1084, VER.크루스칼

'''
import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nodes = [(tuple(map(int,input().split())),i) for i in range(n)]
graph = [[] for _ in range(n)]

for i in range(3):
    nodes.sort(key=lambda x: x[0][i])
    for j in range(n-1):
        no1,ni1 = nodes[j]
        no2,ni2 = nodes[j+1]
        graph[ni1].append((ni2,abs(no1[i] - no2[i])))
        graph[ni2].append((ni1,abs(no1[i] - no2[i])))

vis = [False] * (n+1)

q = [(0,0)]
res = 0

while q:
    wei,nv = heapq.heappop(q)
    if vis[nv]:
        continue

    vis[nv] = True
    res += wei

    for v,w in graph[nv]:
        if not vis[v]:
            heapq.heappush(q,(w,v))
    
print(res)
'''
# 제출 번호 : 102630928, 메모리 : 147256, 시간 : 1768 VER.프림 