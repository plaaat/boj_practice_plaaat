li = []
while True:
  wo = input()
  if wo == '#':
    break
  li.append(list(wo))
oh = ('a','e','i','o','u','A','E','I','O','U')
for i in li:
  n = 0
  for j in i:
    if j in oh:n+=1
  print(n)#  제출 번호 : 80121140, 메모리 : 31120, 시간 : 40