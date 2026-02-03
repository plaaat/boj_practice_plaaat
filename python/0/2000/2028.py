import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = input()
    sqn = str(int(n) ** 2)
    l = len(sqn)

    if sqn[l-len(n):l] == n:
        print('YES')
    else:
        print('NO')

# 제출 번호 : 102597637, 메모리 : 32412, 시간 : 36