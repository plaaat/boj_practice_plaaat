n,m = map(int,input().split())
ban = (str(m)[-1],str(2*m)[-1])
li = []
pn = 0
for i in range(1,n+1):
    i = str(i)
    if not i[-1] in ban:
        li.append(i)
        pn+=1
print(pn)
if pn != 0:
    print(*li)#  ���� ��ȣ : 81176190, �޸� : 38180, �ð� : 92