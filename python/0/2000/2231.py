a = int(input())
if a <10 or a == 0:
    b = 1
elif 10<= a <= 18:
  b = 10
else:
    b = len(str(a))*9
c = a-b-1
e =[]
for i in range(b):
    c+=1
    d = 0
    for s in range(len(str(c))):
        d += int(str(c)[s])
    if a == c+d:
        e.append(a-d)
try:
    print(sorted(e)[0])
except:
    if 1 < a < 10:
        print(int(a/2))
    else:
      print("0")#  제출 번호 : 79658728, 메모리 : 31120, 시간 : 40