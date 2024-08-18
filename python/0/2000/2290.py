import sys

input = lambda: sys.stdin.readline().rstrip()

n, a = map(int, input().split())
a = str(a)


def lcd(a):
  global n
  li = [[' ' for _ in range(n + 2)] for _ in range(2 * n + 3)]
  for num in a:
    if num == '0':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][0] = '|'
        li[i][-1] = '|'
        li[n + 1 + i][0] = '|'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    elif num == '1':
      for i in range(1, n + 1):
        li[i][-1] = '|'
        li[n + 1 + i][-1] = '|'
    elif num == '2':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][-1] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][0] = '|'
        li[-1][i] = '-'
    elif num == '3':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][-1] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    elif num == '4':
      for i in range(1, n + 1):
        li[i][0] = '|'
        li[i][-1] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][-1] = '|'
    elif num == '5':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][0] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    elif num == '6':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][0] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][0] = '|'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    elif num == '7':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][-1] = '|'
        li[n + 1 + i][-1] = '|'
    elif num == '8':
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][0] = '|'
        li[i][-1] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][0] = '|'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    else:
      for i in range(1, n + 1):
        li[0][i] = '-'
        li[i][0] = '|'
        li[i][-1] = '|'
        li[n + 1][i] = '-'
        li[n + 1 + i][-1] = '|'
        li[-1][i] = '-'
    return li


pli = []
for i in a:
  pli.append(lcd(i))
for i in range(2 * n + 3):
  for j in range(len(a)):
    print(*pli[j][i], end=' ', sep='')
  print()

# 제출 번호 : 82635138, 메모리 : 31120, 시간 : 32
