import sys
input = lambda:sys.stdin.readline().rstrip()

dal = [list(map(int,range(1,32))),list(map(int,range(1,30))),list(map(int,range(1,32))),list(map(int,range(1,31))),list(map(int,range(1,32))),list(map(int,range(1,31))),list(map(int,range(1,32))),list(map(int,range(1,32))),list(map(int,range(1,31))),list(map(int,range(1,32))),list(map(int,range(1,31))),list(map(int,range(1,32)))]
for _ in range(int(input())):
  li = list(map(int,input().split()))
  num = 0
  for i in range(12):
    if i == 9:
      if li[0] == 1 or li[1] == 1:
        continue
    elif i == 10:
      if li[1] == 1:
        continue
    elif i == 11:
      if li[1] == 1 or li[2] == 1:
        continue
    else:
      if li[i+1] == 1:
        continue
    for s in dal[i]:
      s = str(s)
      tf = True
      for j in s:
        j = int(j)
        if li[j] == 1:
          tf = False
      if tf:num+=1
  print(num)#  제출 번호 : 79646348, 메모리 : 31120, 시간 : 192