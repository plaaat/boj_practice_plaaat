a = int(input())
b = sorted(list(map(int,input().split())))
c = b[a-1]
d = []
for i in range(a):
  d.append((b[i]/c)*100)
print(sum(d)/a)#  ���� ��ȣ : 79658682, �޸� : 31252, �ð� : 44