import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

v,e = map(int,input().split())
edges = []

for _ in range(e):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((c,a,b))

edges.sort()
par = [i for i in range(v)]

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
for c,a,b in edges:
    if find_p(par,a) != find_p(par,b):
        uni(par,a,b)
        res += c

print(res)

# 제출 번호 : 101855565, 메모리 : 50824, 시간 : 332