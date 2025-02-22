import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
a,b = map(int,input().split())

maps = [input() for _ in range(n)]
minn = float('inf')

def cal(cost,midtf,x,y,k,stx,sty):
    global minn

    if (x - stx) == (y - sty) == k * 3 - 1:
        if maps[y][x] == '.':
            cost += a
        for tx in range(m):
            for ty in range(n):
                if stx <= tx <= x and sty <= ty <= y:
                    continue
                if maps[ty][tx] == '#':
                    cost += b
        minn = min(minn,cost)
        return
    
    if not midtf:
        if maps[y][x] == '.':
            cost += a
        x += 1
        if x - stx == k * 3:
            x = stx
            y += 1
            if y - sty == k:
                midtf = True
    else:
        if x - stx < k:
            if maps[y][x] == '.':
                cost += a
            x += 1
        else:
            if maps[y][x] == '#':
                cost += b
            x += 1
            if x - stx == k * 3:
                x = stx
                y += 1
                if y - sty == k * 2:
                    midtf = False
    if x == m:return
    if y == n:return
    if cost > minn:return
    cal(cost,midtf,x,y,k,stx,sty)    

for i in range(1,7):
    for x in range(m):
        for y in range(n):
            cal(0,False,x,y,i,x,y)

print(minn)

# 제출 번호 : 89995587, 메모리 : 32472, 시간 : 128