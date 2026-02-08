import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]

vis = [[None] * (2 ** n) for _ in range(n)]

def find(x, no):
    if x == ((2 ** n) - 1):
        if li[no][0] != 0:
            return li[no][0]
        else:
            return float('inf')
    
    if vis[no][x]:
        return vis[no][x]
    
    minv = float('inf')
    for i in range(1, n):
        if li[no][i] != 0 and x & (1<<i) == 0:
            minv = min(minv,find(x | (1<<i),i) + li[no][i])
    vis[no][x] = minv

    return minv

print(find(1,0))

# 제출 번호 : 102744089, 메모리 : 48856, 시간 : 980