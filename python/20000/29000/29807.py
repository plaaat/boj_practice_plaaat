n = int(input())
li = list(map(int,input().split()))
pn = 0

for _ in range(5):
    li.append(0)
    
if li[0] > li[2]:
    pn += (li[0]-li[2]) * 508
else:
    pn += (li[2]-li[0]) * 108

if li[1] > li[3]:
    pn += (li[1] - li[3]) * 212
else:
    pn += (li[3] - li[1]) * 305

pn+= li[4] * 707
print(pn*4763)


#  제출 번호 : 82805935, 메모리 : 31120, 시간 : 32