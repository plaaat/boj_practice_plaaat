import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
li = [list(map(int, input())) for _ in range(n)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs():
    q = deque([(0, 0, 0, 1)])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while q:
        x, y, z, num = q.popleft()
        
        if x == m - 1 and y == n - 1:
            return num

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if li[ny][nx] == 0 and not visited[ny][nx][z]:
                    visited[ny][nx][z] = 1
                    q.append((nx, ny, z, num + 1))
                elif li[ny][nx] == 1 and z == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = 1
                    q.append((nx, ny, 1, num + 1))

    return -1

result = bfs()
print(result)#  제출 번호 : 81465924, 메모리 : 303524, 시간 : 1432