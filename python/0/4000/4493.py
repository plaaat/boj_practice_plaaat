t = int(input())
for _ in range(t):
  n = int(input())
  p1 = 0
  for _ in range(n):
    a,b = input().split()
    if a == b:
      continue
    elif a == 'R':
      if b == 'P': p1+=1
      else:p1-=1
    elif a == 'P':
      if b == 'S':p1+=1
      else:p1-=1
    else:
      if b == 'R':p1+=1
      else:p1-=1
  if p1 == 0:print('TIE')
  elif p1<0:print('Player 1')
  else:print('Player 2')#  제출 번호 : 80120312, 메모리 : 31120, 시간 : 2104