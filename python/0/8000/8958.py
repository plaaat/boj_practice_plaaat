for i in range(int(input())):
  a = input()
  b,c = 0,0
  for s in range(len(a)):
    if a[s] == "O":
      b += 1
      c += b
    else:
      b = 0
  print(c)#  ���� ��ȣ : 79658760, �޸� : 31120, �ð� : 52