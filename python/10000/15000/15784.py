import sys
input = lambda:sys.stdin.readline().rstrip()
n,a,b = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
x = li[a-1][b-1]
if x != max(li[a-1]):
  print('ANGRY')
else:
  tf = True
  for i in li:
    if x < i[b-1]:
      print('ANGRY')
      tf = False
      break
  if tf:
    print('HAPPY')#  제출 번호 : 79646492, 메모리 : 66600, 시간 : 236