b = []
for i in range(10):
  a = int(input())
  a = a%42
  if b.count(a)>0:
    continue
  else:
    b.append(a)
print(len(b))#  ���� ��ȣ : 79658850, �޸� : 31252, �ð� : 32