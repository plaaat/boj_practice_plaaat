a,b = map(int, input().split())
c = []
d = []
l = []
for i in range(a):
    e = list(map(int,input().split()))
    c.append(e)

for i in range(a):
    f = list(map(int,input().split()))
    d.append(f)

for i in range(a):
  for s in range(b):
    h = c[i][s]+d[i][s]
    l.append(h)
  print(*l)
  l = []#  ���� ��ȣ : 79659062, �޸� : 31120, �ð� : 52