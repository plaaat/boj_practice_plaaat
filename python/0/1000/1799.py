import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

bish = [[],[]]
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            bish[(i+j) % 2].append((i,j))

vis1 = [False] * (2 * n)
vis2 = [False] * (2 * n)

def btr(cn, bn, x):
    tx = x

    for i in range(bn,len(bish[cn])):
        ny,nx = bish[cn][i]
        v1 = ny - nx + 1
        v2 = ny + nx
        if not vis1[v1] and not vis2[v2]:
            vis1[v1] = True
            vis2[v2] = True
            tx = max(btr(cn,i+1,x+1),tx)
            vis1[v1] = False
            vis2[v2] = False
    
    return tx


print(btr(0,0,0) + btr(1,0,0))