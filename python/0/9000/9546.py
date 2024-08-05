import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num = 0
    for _ in range(n):
        num+=0.5
        num*=2
    print(int(num))#  제출 번호 : 81953817, 메모리 : 31120, 시간 : 48