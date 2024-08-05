import sys
input=lambda:sys.stdin.readline().rstrip()

def noga(n):
  global a
  if n <= 0:
    a+=1
    return
  elif n-2 < 0:
    a+=1
    return
  elif n-3 < 0:
    a+=2
    return
  else:
    noga(n-3)
    noga(n-2)
    return noga(n-1)
for _ in range(int(input())):
  li = {}
  n = int(input())
  a = 0
  noga(n)
  print(a)
  
#  제출 번호 : 79649940, 메모리 : 31120, 시간 : 40