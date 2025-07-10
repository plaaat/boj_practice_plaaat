import sys
input = lambda: sys.stdin.readline().rstrip()

a = 0
t = 0
n = int(input())
while a <= n:
    t += 1
    a = (t*(t+1))//2

if t % 2:
    print(a-n)
else:
    print(0)

# 제출 번호 : 96198313, 메모리 : 32412, 시간 : 44