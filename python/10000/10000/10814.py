import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    y, n = input().split()
    y = int(y)
    b.append([y, i, n])
b.sort()
for s in b:
    print(s[0], s[2])



#  제출 번호 : 79658552, 메모리 : 133376, 시간 : 368