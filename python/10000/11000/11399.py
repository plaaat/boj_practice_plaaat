import sys
input = sys.stdin.readline

n = int(input())
a = 0
nl = list(map(int,input().split()))
nl.sort()
n+=1
for i in nl:
  n-=1
  a+=i*n
print(a)#  ���� ��ȣ : 79650094, �޸� : 31120, �ð� : 44