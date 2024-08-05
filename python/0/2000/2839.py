n = int(input())
a = 0
if n == 4 or n == 7:
  print("-1")
elif n == 3 or n == 5:
  print("1")
else:
  while True:
    if n == 6 or n == 8 or n == 10:
      print(a+2)
      break
    elif n == 7 or n == 9:
      print(a+3)
      break
    a+=1
    n-=5#  제출 번호 : 79658571, 메모리 : 31120, 시간 : 36