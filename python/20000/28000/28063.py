import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x,y = map(int,input().split())

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    res = 4
    if x == 1 or x == n:
        res -= 1
    if y == 1 or y == n:
        res -= 1
    print(res)

# 제출 번호 : 95756019, 메모리 : 32412, 시간 : 40