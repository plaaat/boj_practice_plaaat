import sys

input = sys.stdin.readline

x = []

m = int(input())

for _ in range(m):

  a,b = map(int,input().split())

  x.append([a,b])

x.sort()

for i in range(m):

  print(*x[i])#  ���� ��ȣ : 79658430, �޸� : 122664, �ð� : 372