k = int(input())
for _ in range(k):
  p,m = map(int,input().split())
  n = 0 
  s = set()
  for _ in range(p):
    a = int(input())
    if a in s:
      n+=1
    else:s.add(a)
  print(n)#  ���� ��ȣ : 80120700, �޸� : 31252, �ð� : 136