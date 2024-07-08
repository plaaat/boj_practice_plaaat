import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(max(int(input()),int(input())))
        continue
    li = [list(map(int,input().split())) for _ in range(2)]
    li[0][1] += li[1][0]
    li[1][1] += li[0][0]
    for i in range(2,n):
        li[0][i] += max(li[1][i-1],li[1][i-2])
        li[1][i] += max(li[0][i-1],li[0][i-2])
    print(max(li[0][-1],li[1][-1]))