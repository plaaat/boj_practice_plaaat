t = int(input())

for _ in range(t):

  a,b = input().split()

  a = list(a)

  for i in list(b):

    try:a.remove(i)

    except:break

  if len(a) == 0:print("Possible")

  else:print("Impossible")#  제출 번호 : 79641582, 메모리 : 31120, 시간 : 432