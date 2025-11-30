import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = input()
n2 = s.count('2')
ne = n - n2

if n2 == ne:
    print('yee')
else:
    print('2' if n2 > ne else 'e')

# 제출 번호 : 99278014, 메모리 : 32412, 시간 : 36