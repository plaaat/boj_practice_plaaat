a,b,c = map(int,input().split())
if a == b == c:
  print(a*1000+10000)
elif a!= b and b!= c and c!= a:
  print(max(a,b,c)*100)
else:
  if a == b:
    print(a*100+1000)
  else:
    print(c*100+1000)#  ���� ��ȣ : 80121649, �޸� : 31120, �ð� : 40