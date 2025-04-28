import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
wo = input()
wli = [0 if i == 'B' else (1 if i == 'L' else 2) for i in wo]
q = deque()
vis = [[0] * (3*n) for _ in range(3*n)]
res = 0

f,b = 0,3 * n - 1
vis[f][b] = 1

if wli[f] == 0:
    q.append((0,1,b))
    vis[1][b] = 1
if wli[b] == 0:
    q.append((0,0,b-1))
    vis[0][b-1] = 1

while q:
    for _ in range(len(q)):
        w, f, b = q.popleft()

        if f > b:
            continue
        if f < 3 * n-1 and wli[f] == (w + 1) % 3 and not vis[f+1][b]:
            q.append(((w + 1) % 3, f + 1, b))
            vis[f+1][b] = 1
        if b >= 0 and wli[b] == (w + 1) % 3 and not vis[f][b - 1]:
            q.append(((w+1)%3, f, b-1))
            vis[f][b-1] = 1
    res += 1

print(res)

# 제출 번호 : 93673179, 메모리 : 50084, 시간 : 100