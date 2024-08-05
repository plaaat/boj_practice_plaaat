a,b = map(int,input().split())
c = list(map(int,input().split()))
c = sorted(c)
num = []
for i in range(a):
  for w in range(a-1):
    e = a-w
    for s in range(a-2):
      f = c[e-1]+c[i]+c[s+2]
      if f > b:
        continue
      elif (c[e-1]==c[i]) or (c[i]==c[s+2]) or (c[e-1]==c[s+2]):
        break
      else:
        num.append(f)
print(sorted(num)[len(num)-1])#  제출 번호 : 79658714, 메모리 : 138600, 시간 : 156