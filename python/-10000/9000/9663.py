import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
mn = 0

vis = [0] * n
vis1 = [0] * (2 * n - 1)
vis2 = [0] * (2 * n - 1)

def solve(y):
    global mn
    if y == n:
        mn += 1
        return

    for x in range(n):
        if not vis[x] and not vis1[y - x + n - 1] and not vis2[y + x]:
            vis[x] = vis1[y - x + n - 1] = vis2[y + x] = 1
            solve(y + 1)
            vis[x] = vis1[y - x + n - 1] = vis2[y + x] = 0

solve(0)
print(mn)