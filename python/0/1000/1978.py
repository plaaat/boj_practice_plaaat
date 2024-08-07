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
print(a)


#  제출 번호 : 79658738, 메모리 : 31120, 시간 : 36