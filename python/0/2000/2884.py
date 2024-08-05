a,b = map(int,input().split())
if a == 0:
  if b < 45:
    print(23, ((b+60)-45))
  else:
    print(a, b-45)
elif b < 45:
  print((a-1), ((b+60)-45))
else:
  print(a, b-45)#  제출 번호 : 79658872, 메모리 : 31120, 시간 : 44