t = int(input())
a1,b1 = 100,100
for _ in range(t):
    a,b = map(int,input().split())
    if a>b:
        b1-=a
    elif a<b:
        a1-=b
print(a1,b1,sep="\n")
#  ���� ��ȣ : 79684974, �޸� : 31120, �ð� : 40