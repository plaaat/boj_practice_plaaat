a = int(input())
b = list(input())
d = 0
for i in range(a):
  c = ord(b[i])-96
  d+=c*((31)**(i))

print(d%1234567891)#  ���� ��ȣ : 79658658, �޸� : 31120, �ð� : 44