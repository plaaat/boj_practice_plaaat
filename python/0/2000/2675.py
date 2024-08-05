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
    break#  제출 번호 : 79658997, 메모리 : 31120, 시간 : 40