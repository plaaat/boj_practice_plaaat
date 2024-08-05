t = int(input())
a1,b1 = 100,100
for _ in range(t):
    a,b = map(int,input().split())
    if a>b:
        b1-=a
    elif a<b:
        a1-=b
print(a1,b1,sep="\n")
#  제출 번호 : 79684974, 메모리 : 31120, 시간 : 40