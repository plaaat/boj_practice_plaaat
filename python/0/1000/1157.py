a = input()
d,e = 0,0
for i in range(0,26):
  b = a.count(chr(i+65))
  c = a.count(chr(i+97))
  if b+c > d:
    d = b+c
    e = i
  elif b+c == d:
    e = 9999
if e == 9999:
  print("?")
else:
  print(chr(e+65))#  ���� ��ȣ : 79658778, �޸� : 33076, �ð� : 76