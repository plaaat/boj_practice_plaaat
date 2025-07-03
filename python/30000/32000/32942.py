import sys
input = lambda: sys.stdin.readline().rstrip()

a,b,c = map(int,input().split())

vis = [[] for _ in range(11)]

for x in range(1,11):
    for y in range(1,11):
        if a * x + b * y == c:
            vis[x].append(y)

for i in range(1,11):
    if vis[i]:
        print(*vis[i])
    else:
        print(0)

# 제출 번호 : 95921275, 메모리 : 32412, 시간 : 40