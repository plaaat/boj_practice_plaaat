b = []
for i in range(10):
  a = int(input())
  a = a%42
  if b.count(a)>0:
    continue
  else:
    b.append(a)
print(len(b))#  제출 번호 : 79658850, 메모리 : 31252, 시간 : 32