import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    tn = 1
    dis = 2
    while True:
        td = tn * (tn + 1)
        if td - tn >= d:
            print(dis - 1)
            break
        if td >= d:
            print(dis)
            break
        tn += 1
        dis += 2

# 제출 번호 : 93609936, 메모리 : 32412, 시간 : 784