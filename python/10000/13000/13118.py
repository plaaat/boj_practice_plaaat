li = list(map(int,input().split()))
x,y,r = map(int,input().split())
if x in li:
  print(li.index(x)+1)
else:print(0)#  제출 번호 : 80120071, 메모리 : 31120, 시간 : 40