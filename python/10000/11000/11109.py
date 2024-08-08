import sys

input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    a += d * b
    b *= c
    if a > b:
        print("do not parallelize")
    elif a < b:
        print("parallelize")
    else:
        print("does not matter")


#  제출 번호 : 82202018, 메모리 : 31120, 시간 : 32
