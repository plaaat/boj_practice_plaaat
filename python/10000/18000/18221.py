import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = []
fr = set()
for i in range(n):
    tl = list(map(int,input().split()))
    for s in range(n):
        if tl[s] == 1:
            fr.add((s,i))
        elif tl[s] == 2:
            sx = s
            sy = i
        elif tl[s] == 5:
            kx = s
            ky = i

if (sy-ky) ** 2 + (sx-kx) ** 2 < 25 or len(fr) < 3:
    print(0)
else:
    pn = 0
    for i in range(min(sx,kx),max(sx,kx)+1):
        if pn==3:break
        for s in range(min(sy,ky),max(sy,ky)+1):
            if (i,s) in fr:
                pn += 1
            if pn == 3:break

    if pn < 3:
        print(0)
    else:
        print(1)


#  제출 번호 : 84732799, 메모리 : 90512, 시간 : 540