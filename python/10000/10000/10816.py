import sys

input = sys.stdin.readline
a = int(input())
fl = [0] * (20000001)
b = list(map(int, input().split()))
for i in range(a):
    fl[b[i] + 10000000] += 1
c = int(input())
d = list(map(int, input().split()))
e = []
for i in range(c):
    e.append(fl[d[i] + 10000000])
print(*e)


#  제출 번호 : 79654292, 메모리 : 388560, 시간 : 556
