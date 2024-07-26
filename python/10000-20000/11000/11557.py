import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    wo = ''
    mn = -1
    for _ in range(n):
        a,b = input().split()
        b = int(b)
        if mn<b:
            wo = a
            mn = b
    print(wo)