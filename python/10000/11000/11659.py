import sys
input=lambda:sys.stdin.readline().rstrip()

n,m = map(int, input().split())
a = 0
li = tuple(map(int,input().split()))
pl = [0]
for i in li:
  a+=i
  pl.append(a)
for _ in range(n):
  try:
    i,j = map(int,input().split())
    print(pl[j]-pl[i-1])
  except:
    break#  ���� ��ȣ : 79650012, �޸� : 41240, �ð� : 280