a,b = map(int,input().split())
n,m = divmod(a,b)
if a !=0 and m<0:
  print(n+1)
  print(m-b)
else:
  print(n)
  print(m)#  ���� ��ȣ : 79800609, �޸� : 31120, �ð� : 48