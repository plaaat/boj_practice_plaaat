a,b = map(int,input().split())
n,m = divmod(a,b)
if a !=0 and m<0:
  print(n+1)
  print(m-b)
else:
  print(n)
  print(m)#  제출 번호 : 79800609, 메모리 : 31120, 시간 : 48