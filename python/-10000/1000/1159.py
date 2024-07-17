import sys
input = lambda:sys.stdin.readline().rstrip()

dic = {}
pli = []
t = int(input())
tf = True
for _ in range(t):
    wo = input()
    fwo = wo[0]
    if fwo in dic:
        if dic[fwo] == 4:
            tf = False
            pli.append(fwo)
        dic[fwo]+=1
    else:dic[fwo] = 1
if tf:print('PREDAJA')
else:
    pli.sort()
    print(*pli,sep ='')