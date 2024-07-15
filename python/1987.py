import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

def dfs(a,b,vis,num):
    global mn
    mn = max(mn,num)
    for x,y in d:
        if y+a<0 or y+a>(n-1) or b+x<0 or b+x>(m-1):
            continue
        wo = li[a+y][b+x]
        if not wo in vis:
            vis.add(wo)
            dfs(a+y,b+x,vis,num+1)
            vis.remove(wo)

n,m = map(int,input().split())
li = [list(input()) for _ in range(n)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
mn = -1
dfs(0,0,set(li[0][0]),1)
print(mn)

#pypy로 쇼부봄 ㅇㅅㅇㅅㅇ