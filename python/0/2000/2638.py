import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
d = [(0,1),(0,-1),(1,0),(-1,0)]
cli = [list(map(int,input().split())) for _ in range(n)]
q = deque([(0,0)])
cli[0][0] = -1
time = -1

while q:
    tq = deque([])
    while q:
        x,y = q.popleft()
        for dx, dy in d:
            dx += x
            dy += y
            if 0 <= dx < m and 0 <= dy < n:
                if cli[dy][dx] == -1:
                    continue
                if cli[dy][dx] == 0:
                    cli[dy][dx] = -1
                    q.append((dx,dy))
                elif cli[dy][dx] == 1:
                    cli[dy][dx] = 2
                else:
                    cli[dy][dx] = -1
                    tq.append((dx,dy))
    q = tq
    time += 1
print(time)

# 제출 번호 : 101667504, 메모리 : 34968, 시간 : 72
'''
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
d = [(0,1),(0,-1),(1,0),(-1,0)]
cli = [list(map(int,input().split())) for _ in range(n)]

def airs(x,y):
    global cli

    airq = deque([(x,y)])
    cli[y][x] = -1
    while airq:
        nowX, nowY = airq.popleft()
        for dx, dy in d:
            dx += nowX
            dy += nowY
            if (0 <= dx < m and 0 <= dy < n) and cli[dy][dx] == 0:
                cli[dy][dx] = -1
                airq.append((dx,dy))
airs(0,0)

def chkair(x,y):
    a = False
    for dx, dy in d:
        dx += x
        dy += y
        if (0 <= dx < m and 0 <= dy < n) and cli[dy][dx] == -1:
            if a:
                return True
            a = True
    return False

times = 0
def find():
    global times

    airchli = []
    for i in range(n):
        for j in range(m):
            if cli[i][j] == 1:
                if chkair(j,i):
                    airchli.append((j,i))

    if not airchli:
        return

    for x, y in airchli:
        cli[y][x] = -1
        for dx, dy in d:
            dx += x
            dy += y
            if (0 <= dx < m and 0 <= dy < n) and cli[dy][dx] == 0:
                airs(dx,dy)
    times += 1
    find()

find()
print(times)

# 제출 번호 : 101666660, 메모리 : 35016, 시간 : 300
'''