a = input().split()
c = []
d = 0
for i in range(5):
  b = int(a[i])**2
  c.append(b)
for i in range(5):
  d += c[i]
print(d%10)#  ���� ��ȣ : 79659082, �޸� : 31120, �ð� : 40