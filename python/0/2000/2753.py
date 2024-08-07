a = int(input())
if(a%400 == 0):
    print("1")
else:
  if(a%100 == 0):
    print("0")
  else:
       if(a%4 == 0):
          print("1")
       else:
          print("0")


#  제출 번호 : 79659403, 메모리 : 31120, 시간 : 40