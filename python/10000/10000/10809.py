a = list(input())
b = []
for s in range(26):
  if a.count(chr(97+s)) > 0:
    b.append(a.index(chr(97+s)))
  else:
    b.append(-1)
print(*b)#  ���� ��ȣ : 79658799, �޸� : 31120, �ð� : 44