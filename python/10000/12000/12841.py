import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
cross = list(map(int, input().split()))
lft = list(map(int, input().split()))
rgt = list(map(int, input().split()))

lfts = [0] * (n + 1)
rgts = [0] * (n + 1)

for i in range(1, n):
    lfts[i] = lfts[i - 1] + lft[i - 1]
    rgts[n - i] = rgts[n - i + 1] + rgt[n - i - 1]

minn = float('inf')
cres = 0

for i in range(1, n + 1):
    sumn = cross[i - 1] + lfts[i - 1] + rgts[i]
    if sumn < minn:
        minn = sumn
        cres = i

print(cres, minn)

# 제출번호 : 90112738, 메모리 : 54712, 시간 : 180