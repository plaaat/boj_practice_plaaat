a = input().split()
for i in range(7):
  if int(a[i])+1 == int(a[i+1]):
    b = 0
  elif int(a[i])-1 == int(a[i+1]):
    b = 1
  else:
    b = 2
    break
if b == 0:
  print("ascending")
elif b == 1:
  print("descending")
else:
  print("mixed")#  ���� ��ȣ : 79658769, �޸� : 31120, �ð� : 40