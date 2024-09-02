import sys
input = lambda: sys.stdin.readline().rstrip()
def chk(li):
    if li[0][0] + li[1][1] + li[2][2] != 15:
        return False
    if li[0][2] + li[1][1] + li[2][0] != 15:
        return False
    for i in range(3):
        tn = 0
        for j in range(3):
            tn += li[j][i]
        if tn != 15:
            return False
    return True
vis = set()

def dfs(x,r,li):
    global pn
    if x == 9:
        if chk(li):
            pn = min(pn,sum(abs(org[i][j] - li[i][j]) for i in range(3) for j in range(3)))
    if x > 2 and x % 3 == 0:
        if sum(li[r]) != 15:
            return
        r += 1
    for i in range(1,10):
        if not i in vis and sum(li[r]) + i <= 15:
            vis.add(i)
            li[r][x%3] = i
            dfs(x+1,r,li)
            vis.remove(i)
            li[r][x%3] = 0

org = [list(map(int,input().split())) for _ in range(3)]
li = [[0 for _ in range(3)] for _ in range(3)]

pn = float('inf')
dfs(0,0,li)
print(pn)

# 제출 번호 : 83323891, 시간 : 31252, 메모리 : 48