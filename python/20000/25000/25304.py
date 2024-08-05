tn = int(input())
n = 0
t = int(input())
for _ in range(t):
  a,b = map(int,input().split())
  n+=a*b
if n == tn:
  print('Yes')
else:
  print('No')#  제출 번호 : 80125767, 메모리 : 31120, 시간 : 44