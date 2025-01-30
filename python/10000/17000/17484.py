import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

d = (1, 0, -1)
mn = float("inf")
li = [list(map(int, input().split())) for _ in range(n)]


def dfs(a, b, c, nn):
    global mn
    if b == n:
        mn = min(nn, mn)
        return
    for i in d:
        if 0 <= i + a < m and i != c and not li[b][i + a] + nn > mn:
            dfs(a + i, b + 1, i, li[b][i + a] + nn)


for i in range(m):
    dfs(i, 0, 2, 0)
print(mn)



#  제출 번호 : 83719644, 메모리 : 31252, 시간 : 32