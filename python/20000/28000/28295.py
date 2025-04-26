import sys
input = lambda: sys.stdin.readline().rstrip()

a = sum(int(input()) for _ in range(10)) % 4
if a == 0:
    print('N')
elif a == 1:
    print('E')
elif a == 2:
    print('S')
else:
    print('W')

# 제출 번호 : 93217025, 메모리 : 32412, 시간 : 36