a = int(input())
b = list(map(int,input().split()))
for i in range(a):
    if b[i] == 1:
        a-=1
        continue
    else:
     for s in range(b[i]-1):
        s += 2
        if b[i] == s:
            break
        elif b[i]%s == 0:
            a -= 1
            break
        else:
            continue
print(a)#  ���� ��ȣ : 79658738, �޸� : 31120, �ð� : 36