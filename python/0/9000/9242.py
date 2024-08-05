import sys

input = lambda:sys.stdin.readline()

li = [input() for _ in range(5)]

le = (len(li[0])//4)

num = [['***','* *','* *','* *','***'], ['  *','  *','  *','  *','  *'], ['***','  *','***','*  ','***'], ['***','  *','***','  *','***'],['* *','* *','***','  *','  *'],['***','*  ','***','  *','***'],['***','*  ','***','* *','***'],['***','  *','  *','  *','  *'],['***','* *','***','* *','***'],['***','* *','***','  *','***']]

pn = []

tf = True

for i in range(le):

  fal = 0

  for w in range(10):

    n = 0

    for s in li:

      if s[i*4:i*4+3] == num[w][n]:

          n+=1

    if n == 5:

      pn.append(w)

      break

    else:

      fal+=1

  if fal == 10:

    tf = False

    break

a = "0"

for i in pn:

  a = a+str(i)

pn = int(a)

if tf and pn%6==0:

  print("BEER!!")

else:

  print("BOOM!!")#  제출 번호 : 79646279, 메모리 : 31120, 시간 : 40