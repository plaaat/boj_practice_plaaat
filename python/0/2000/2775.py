for i in range(int(input())):
  a = int(input())
  b = int(input())
  c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
  d = []
  for l in range(b):
    d.append(sum(c[:l+1]))
  if a == 0:
    print(c[b-1])
  elif a == 1:
    print(d[b-1])
  else:
    e = list(d)
    for k in range(a-1):
      d = list(e)
      for s in range(b):
        e[s] = (sum(d[:s+1]))
    print(e[b-1])#  제출 번호 : 79658591, 메모리 : 31120, 시간 : 56