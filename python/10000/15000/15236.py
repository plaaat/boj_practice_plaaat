import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
num = 0
for i in range(n+1):
  num+=i
  for s in range(n+1):
    num+=s
print(num)#  ���� ��ȣ : 79646484, �޸� : 31120, �ð� : 124