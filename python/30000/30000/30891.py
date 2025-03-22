import sys
input = lambda: sys.stdin.readline().rstrip()

n,r = map(int,input().split())

xli,yli = [],[]

for _ in range(n):
    x,y = map(int,input().split())
    xli.append(x)
    yli.append(y)

mix = min(xli)
mx = max(xli)
miy = min(yli)
my = max(yli)
cnt = -1
rx,ry = 0,0
for i in range(mix,mx+1):
    for j in range(miy,my+1):
        t = 0
        for a in range(n):
            x,y = xli[a],yli[a]
            if ((x-i)**2 + (y - j)**2) ** 0.5 <= r:
                t += 1
        if t > cnt:
            cnt = t
            rx = i
            ry = j
print(rx,ry)

# 제출번호 : 91838756, 메모리 : 32412, 시간 : 2048