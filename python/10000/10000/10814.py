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
#  ���� ��ȣ : 79658552, �޸� : 133376, �ð� : 368