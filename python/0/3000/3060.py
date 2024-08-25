import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    sun = sum(li)
    d = 1
    while sun <= n:
        d+=1
        sun*=4
    print(d)


# 