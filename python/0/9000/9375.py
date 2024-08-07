import sys
input=lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
  n = int(input())
  dic = {}
  li = set()
  for _ in range(n):
    a,b = map(str,input().split())
    li.add(b)
    if not b in dic:
      dic[b] = 1
    else:
      dic[b]+=1
  a = 1
  if len(li) == 1:
    print(dic[li.pop()])
  else:
    for i in range(len(li)):
      num = dic[li.pop()]
      a*=(num+1)
    print(a-1)


#  제출 번호 : 79649971, 메모리 : 31120, 시간 : 44