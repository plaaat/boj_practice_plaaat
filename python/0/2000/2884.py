a,b = map(int,input().split())
if a == 0:
  if b < 45:
    print(23, ((b+60)-45))
  else:
    print(a, b-45)
elif b < 45:
  print((a-1), ((b+60)-45))
else:
  print(a, b-45)#  ���� ��ȣ : 79658872, �޸� : 31120, �ð� : 44