import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
x = [0] + list(map(int,input().split())) +[n]
h = 0

a,b = 0,n
while a <= b:
    t = (a+b)//2
    if (x[1] - x[0] <= t) and (x[-1] - x[-2] <= t):
        for i in range(1, m-2):
            if x[i+1] - x[i]/2 > t:
                break
        else:
            b = t-1
            h = t
    else:
        a = t + 1
print(h)