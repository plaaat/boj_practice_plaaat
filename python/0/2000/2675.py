x = int(input())
while x:
  try:
    a, b = input().split()
    c = []
    for i in range(len(b)):
      for s in range(int(a)):
        c.append(b[i])
    print(*c, sep='')
  except:
    break#  ���� ��ȣ : 79658997, �޸� : 31120, �ð� : 40