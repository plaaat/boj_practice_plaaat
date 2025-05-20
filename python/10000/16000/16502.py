import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
m = int(input())

node = [[],[],[],[],]

for _ in range(m):
    a,b,x = input().split()
    node[ord(a) - 65].append((ord(b) - 65,float(x)))

res = [0,0,0,0]

def dfs(now, per, cnt):
    global res
    if cnt == t:
        res[now] += per * 100
        return
    for nx, n in node[now]:
        dfs(nx, per * n, cnt + 1)

for i in range(4):
    dfs(i,0.25,0)

for r in res:
    print(f'{r:.2f}')

# 제출 번호 : 94558522, 메모리 : 32412, 시간 : 32