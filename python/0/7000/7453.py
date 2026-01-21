import sys
input = lambda: sys.stdin.readline().rstrip()

a,b,c,d = [],[],[],[]
t = int(input())
for _ in range(t):
    q,w,e,r = map(int,input().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)

abset = {}

for i in range(t):
    for j in range(t):
        abset[a[i]+b[j]] = abset.get(a[i]+b[j],0) + 1

res = 0
for i in range(t):
    for j in range(t):
        if (c[i]+d[j]) * -1 in abset:
            res += abset[(c[i]+d[j]) * -1]

print(res)

# 제출 번호 : 102102330, 메모리 : 1190248, 시간 : 9628 By.pypy3