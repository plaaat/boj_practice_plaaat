import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):

  m = round(float(input())/6 ,10)+0.00000000001

  print(str(m)[0:-1])#  ���� ��ȣ : 79641401, �޸� : 31120, �ð� : 44