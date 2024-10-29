import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = range(1,n+1)
li = list(map(int,input().split()))

q = deque()

for i in range(n):
    t = li[n - i -1]
    if t == 1:
        q.appendleft(nli[i])
    elif t == 2:
        nt = q.popleft()
        q.appendleft(nli[i])
        q.appendleft(nt)
    else:
        q.append(nli[i])

print(*q,sep=' ')