import sys

input = lambda: sys.stdin.readline().rstrip()

li = [list(map(int, input().split())) for _ in range(5)]
d = ((0, 1), (1, 0), (-1, 0), (0, -1))
vis = set()
pn = 0


def dfs(x, y, n, an):
  global pn
  if pn == 1 or n == 3:
    if an == 2:
      pn = 1
    return
  if an == 2:
    pn = 1
  for dx, dy in d:
    if pn == 1:
      break
    dx += x
    dy += y
    if -1 < dx < 5 and -1 < dy < 5 and (dx, dy) not in vis:
      if li[dy][dx] == -1:
        vis.add((dx, dy))
      else:
        vis.add((dx, dy))
        if li[dy][dx] == 1:
          dfs(dx, dy, n + 1, an + 1)
        else:
          dfs(dx, dy, n + 1, an)
        vis.remove((dx, dy))


o, m = map(int, input().split())
vis.add((m, o))
dfs(m, o, 0, 0)
print(pn)

# 제출 번호 : 82617023  메모리 : 31120  시간 : 32
