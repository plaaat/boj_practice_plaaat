a,b = map(int,sorted(input().split()))
c = a*b
if b>a: a,b=b,a

while b!=0:
  a=a%b
  a,b=b,a
print(a)
print(int(c/a))#  ���� ��ȣ : 79658643, �޸� : 31120, �ð� : 44