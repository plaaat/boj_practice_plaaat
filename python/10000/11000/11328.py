t = int(input())

for _ in range(t):

  a,b = input().split()

  a = list(a)

  for i in list(b):

    try:a.remove(i)

    except:break

  if len(a) == 0:print("Possible")

  else:print("Impossible")#  ���� ��ȣ : 79641582, �޸� : 31120, �ð� : 432