tn = int(input())
n = 0
t = int(input())
for _ in range(t):
  a,b = map(int,input().split())
  n+=a*b
if n == tn:
  print('Yes')
else:
  print('No')#  ���� ��ȣ : 80125767, �޸� : 31120, �ð� : 44