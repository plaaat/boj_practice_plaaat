import sys
input = lambda: sys.stdin.readline().rstrip()

ma = []
t = int(input())
for _ in range(t):
    ma.append(tuple(map(int, input().split())))

inf = float("inf")
minn = inf
for i in range(t):
    m1,m2 = inf,inf
    ma1 = ma[i]
    for j in range(t):
        if i == j:
            continue
        ma2 = ma[j]
        td = abs(ma1[0] - ma2[0]) + abs(ma1[1] - ma2[1]) + abs(ma1[2] - ma2[2])
        if td < m1:
            m2 = m1
            m1 = td
        elif td < m2:
            m2 = td
    minn = min(m1+m2, minn)
print(minn)