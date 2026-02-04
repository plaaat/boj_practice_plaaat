import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a-1,b-1))
edges.sort()

par = [i for i in range(n)]

def find_p(p,x):
    if p[x] != x:
        p[x] = find_p(p,p[x])
    return p[x]

def uni(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

res = 0
mxc = 0
cnt = 0
for c,a,b in edges:
    if find_p(par,a) != find_p(par,b):
        uni(par,a,b)
        res += c
        mxc = max(mxc,c)
        cnt += 1
    if cnt == n:
        break

print(res - mxc)

# 제출 번호 : 102631972, 메모리 : 196208, 시간 : 3728