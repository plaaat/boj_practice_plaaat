import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a*2<=b and b%a == 0:
        print(1)
    else:
        print(0)
    