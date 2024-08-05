import sys
input = sys.stdin.readline

n = int(input())
pl = [0] * (n + 1)
li = [0] * (n + 1)

for i in range(1, n + 1):
    pl[i] = int(input())
li[1] = pl[1]

for i in range(2, n + 1):
  li[i] = max(li[i - 2], li[i - 3] + pl[i - 1]) + pl[i]

print(li[n])#  제출 번호 : 79650069, 메모리 : 31252, 시간 : 40