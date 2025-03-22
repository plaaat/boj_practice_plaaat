import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
maps = [input() for _ in range(n)]
sx,sy = map(int,input().split())

dw = 'URDL'
dd = ((0,-1),(1,0),(0,1),(-1,0))

h1 = (1,0,3,2)
h2 = (3,2,1,0)

sx -= 1
sy -= 1
mt,md = -1,''
for i in range(4):
    x,y,d,t = sx,sy,i,1
    while True:
        x += dd[d][0]
        y += dd[d][1]
        if (not (0 <= x < m and 0 <= y < n)) or maps[y][x] == 'C':
            break

        if maps[y][x] == '/':
            d = h1[d]
        elif maps[y][x] == '\\':
            d = h2[d]
        t += 1

        if (x,y,d) == (sx,sy,i):
            t = float('inf')
            break
    
    if t == float('inf'):
        mt = 'Voyager'
        md = dw[i]
        break
    else:
        if mt < t:
            mt = t
            md = dw[i]

print(md)
print(mt)

# 제출 번호 : 91837968, 메모리 : 32412, 시간 : 688