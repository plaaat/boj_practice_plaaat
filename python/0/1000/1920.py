import sys
input = sys.stdin.readline
a = int(input())
b = set(input().split())
c = int(input())
d = input().split()
for i in range(c):
  if d[i] in b:
    print(1)
  else:
    print(0)
#  ���� ��ȣ : 79654362, �޸� : 139752, �ð� : 188