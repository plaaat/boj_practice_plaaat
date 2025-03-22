import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
res = 0

if t % 10 != 0:
    print(-1)
else:
    a = t // 300
    t %= 300
    b = t // 60
    t %= 60
    c = t // 10
    print(a,b,c)

# 제출 번호 : 91702753, 메모리 : 32544, 시간 : 44