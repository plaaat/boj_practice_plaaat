import sys
input = lambda: sys.stdin.readline().rstrip()

print(bin(int(input(), 2) * int(input(), 2))[2:])

# 제출 번호 : 101216149, 메모리 : 32412, 시간 : 36