import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n,m,k,x = map(int,input().split())
dic = {}
vis = [float('inf') for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    if not a in dic:
        dic[a] = []
    dic[a].append((b,1))

q = []
heapq.heappush(q,(0,x))
vis[x] = 0
while q:
    a,b = heapq.heappop(q)
    if vis[b] < a or not b in dic:continue
    for i in dic[b]:
        c = a + i[1]
        if c < vis[i[0]]:
            vis[i[0]] = c
            heapq.heappush(q,(c, i[0]))
tf = False
for i in range(1,n+1):
    if vis[i] == k:
      tf = True
      print(i)
if not tf:
  print(-1)


#  제출 번호 : 83998272, 메모리 : 198164, 시간 : 3364