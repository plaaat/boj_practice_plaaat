a,b,c = map(int,input().split())
if a == b == c:
  print(a*1000+10000)
elif a!= b and b!= c and c!= a:
  print(max(a,b,c)*100)
else:
  if a == b:
    print(a*100+1000)
  else:
    print(c*100+1000)#  제출 번호 : 80121649, 메모리 : 31120, 시간 : 40