import sys
input = lambda: sys.stdin.readline().rstrip()


maps = [[''] * 20 for _ in range(20)]
n = int(input())
res = 0
fl = True
ans = -1

for _ in range(n):
    x,y = map(int,input().split())
    if ans != -1:continue
    ty = ('B' if fl else 'W')
    maps[y][x] = ty
    fl = not fl
    res += 1
    if res < 9:continue
    v = h = d = dd = 1
    vp = vm = hp = hm = dp = dm = ddp = ddm = True
    for i in range(1,19):
        if x + i < 20:
            if hp and maps[y][x+i] == ty:
                h += 1
            else:
                hp = False
            if y + i < 20:
                if dp and maps[y+i][x+i] == ty:
                    d += 1
                else:
                    dp = False
        if y + i < 20:
            if vp and maps[y+i][x] == ty:
                v += 1
            else:
                vp = False
        if x - i > 0:
            if hm and maps[y][x-i] == ty:
                h += 1
            else:
                hm = False
            if y - i > 0:
                if dm and maps[y-i][x-i] == ty:
                    d += 1
                else:
                    dm = False
        if y - i > 0:
            if vm and maps[y-i][x] == ty:
                v += 1
            else:
                vm = False
        if ddp and x + i < 20 and y - i > 0 and maps[y - i][x + i] == ty:
            dd += 1
        else:
            ddp = False
        if ddm and x - i > 0 and y + i < 20 and maps[y + i][x - i] == ty:
            dd += 1
        else:
            ddm = False
    if v == 5 or h == 5 or d == 5 or dd == 5:
        ans = res

print(ans)

# 제출 번호 : 96361530, 메모리 : 32412, 시간 : 32