import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]

def find(maps, stak):
    if stak == 5:
        return max(j for i in maps for j in i)
    mxn = -1
    for d in range(4):
        tmap = [i[:] for i in maps]
        if d == 0:
            for i in range(n):
                now = 0
                for j in range(1, n):
                    if tmap[i][j] != 0:
                        tmp = tmap[i][j]
                        tmap[i][j] = 0
                        if tmap[i][now] == 0:
                            tmap[i][now] = tmp
                        elif tmap[i][now] == tmp:
                            tmap[i][now] *= 2
                            now += 1
                        else:
                            now += 1
                            tmap[i][now] = tmp
        elif d == 1:
            for i in range(n):
                now = n-1
                for j in range(n-1, -1, -1):
                    if tmap[i][j] != 0:
                        tmp = tmap[i][j]
                        tmap[i][j] = 0
                        if tmap[i][now] == 0:
                            tmap[i][now] = tmp
                        elif tmap[i][now] == tmp:
                            tmap[i][now] *= 2
                            now -= 1
                        else:
                            now -= 1
                            tmap[i][now] = tmp
        elif d == 2:
            for j in range(n):
                now = n-1
                for i in range(n-1, -1, -1):
                    if tmap[i][j] != 0:
                        tmp = tmap[i][j]
                        tmap[i][j] = 0
                        if tmap[now][j] == 0:
                            tmap[now][j] = tmp
                        elif tmap[now][j] == tmp:
                            tmap[now][j] *= 2
                            now -= 1
                        else:
                            now -= 1
                            tmap[now][j] = tmp
        else:
            for j in range(n):
                now = 0
                for i in range(1, n):
                    if tmap[i][j] != 0:
                        tmp = tmap[i][j]
                        tmap[i][j] = 0
                        if tmap[now][j] == 0:
                            tmap[now][j] = tmp
                        elif tmap[now][j] == tmp:
                            tmap[now][j] *= 2
                            now += 1
                        else:
                            now += 1
                            tmap[now][j] = tmp
        mxn = max(mxn, find(tmap,stak+1))
    return mxn


print(find(maps, 0))

# 제출 번호 : 102441067, 메모리 : 32412, 시간 : 108