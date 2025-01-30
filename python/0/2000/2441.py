import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    for s in range(i):
        print(' ',end='')
    for s in range(n-i):
        print('*',end='')
    print()


#  제출 번호 : 84145316, 메모리 : 31120, 시간 : 32