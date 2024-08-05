def pl():
  a, b = map(int, input().split())
  x = a+b
  if(x > 0):
    y = 1
  else:
    y = 0
  for i in range(0, int(y), 1):
    print(x)
    a = 0
    b = 0
    pl()
pl()#  제출 번호 : 79659287, 메모리 : 31120, 시간 : 48