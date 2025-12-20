# 유니온 파인드 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
knowli = list(map(int,input().split()))[1:]
parent = list(range(n + 1))
party = [list(map(int,input().split())) for _ in range(m)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty

for i in range(m):
    for j in range(1,party[i][0]):
        union(party[i][j],party[i][j+1])

leads = set(find(i) for i in knowli)
ans = 0

for per in party:
    if any(find(p) in leads for p in per[1:]):
        continue
    ans += 1

print(ans)

# 제출 번호 : 101222136, 메모리 : 32412, 시간 : 32

'''
# 걍 뺑뻉이 돌리기
n,m = map(int,input().split())
knowli = set(list(map(int,input().split()))[1:])

party = [list(map(int,input().split()))[1:] for _ in range(m)]
leknowli = len(knowli)

for _ in range(m):
    for per in party:
        if any(p in knowli for p in per):
            knowli.update(per)
    if leknowli == len(knowli):
        break

ans = 0
for per in party:
    if any(p in knowli for p in per):
        continue
    ans += 1

print(ans)

# 제출 번호 : 101221586, 메모리 : 32412, 시간 : 44
'''