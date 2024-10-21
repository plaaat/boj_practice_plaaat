import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        while n != 1:
            if n % 2 == 1:
                print('Gazua')
                break
            n/=2
        else:print('GoHanGang')
    else:print('Gazua')