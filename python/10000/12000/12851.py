import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())

q = deque()
visit = [-1] * 100001
q.append((n,0))
t = -1
x = 0

visit[n] = 0
while q:
    now,time = q.popleft()
    if now == k:
        x += 1
        if t == -1:
            t = time
        continue
    if time == t:
        continue
    if now * 2 <= 100000 and (visit[now * 2] == -1 or visit[now * 2] == time):
        visit[now * 2] = time
        q.append((now * 2,time + 1))
    if now + 1 <= 100000 and (visit[now + 1] == -1 or visit[now + 1] == time):
        visit[now + 1] = time
        q.append((now + 1, time + 1))
    if now - 1 >= 0 and (visit[now - 1] == -1 or visit[now - 1] == time):
        visit[now - 1] = time
        q.append((now - 1, time + 1))

print(t)
print(x)

# 제출 번호 : 90196968, 메모리 : 40360, 시간 : 284