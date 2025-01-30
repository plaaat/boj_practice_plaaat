import sys
input = sys.stdin.readline

for _ in range(3):
    t = int(input())
    n = sum(int(input()) for _ in range(t))
    if n == 0:
        print(0)
    elif n > 0:
        print('+')
    else:
        print('-')


#  제출 번호 : 87783384, 메모리 : 32412, 시간 : 136