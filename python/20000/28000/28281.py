n,m = map(int,input().split())
li = list(map(int,input().split()))
pl = []
for i in range(n-1):
  pl.append((li[i]*m)+(li[i+1]*m))
print(min(pl))#  ���� ��ȣ : 79800391, �޸� : 42036, �ð� : 84