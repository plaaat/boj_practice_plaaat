while True:
  try:
    a = map(int,input().split())
    a = sorted(a)
    if a[0]+a[1]+a[2] == 0:
      break
    elif a[0]**2+a[1]**2==a[2]**2:
      print("right")
    else:
      print("wrong")
  except:
    break#  ���� ��ȣ : 79658750, �޸� : 31120, �ð� : 40