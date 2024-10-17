import sys
input = lambda: sys.stdin.readline().rstrip()

y = input()
y,m,d = y[0:4],y[4:6],y[6:]
t = int(input())
mn = -1
pn = []
cal = lambda x,y: sum((int(x[i]) - int(y[i])) ** 2 for i in range(len(x)))

for _ in range(t):
    tn = 1
    ty = input()
    ty,td,tm = ty[0:4],ty[4:6],ty[6:]
    tn *= cal(y,ty)
    tn *= cal(m,tm)
    tn *= cal(d,td)
    if tn > mn:
        mn = tn
        pn = [(ty,td,tm)]
    elif tn == mn:
        pn.append((ty,td,tm))

print(*sorted(pn)[0],sep='')