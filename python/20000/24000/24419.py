import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

vis = {}
def fac(n):
    if n in vis:
        return vis[n]
    if n <= 1:
        return 1
    else:
        vis[n] = n * fac(n - 1)
        return vis[n]

n = int(input())
for _ in range(n):
    input()

print((fac(n * 2) // fac(n) ** 2) % 1000000007, n ** 2)

# 제출 번호 : 83302755, 메모리 : 32700, 시간 : 56