import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_right as br

input()
a = list(map(int,input().split()))
input()
b = list(map(int,input().split()))

mxn = -1
dica = {}
dicb = {}
for i, x in enumerate(a):
    if not x in dica:
        dica[x] = []
    dica[x].append(i)
    mxn = max(mxn,x)

for i, x in enumerate(b):
    if not x in dicb:
        dicb[x] = []
    dicb[x].append(i)
    mxn = max(mxn,x)

res = []
noa, nob = -1, -1
for i in range(mxn,0,-1):
    if not i in dica or not i in dicb:
        continue
    ta = dica[i]
    tb = dicb[i]

    while True:
       loca = br(ta, noa)
       locb = br(tb, nob)

       if loca < len(ta) and locb < len(tb):
           noa, nob = ta[loca], tb[locb]
           res.append(i)
       else:
           break
           
print(len(res))
if res:
    print(*res)

# 제출 번호 : 102364938, 메모리 : 34476, 시간 : 36
# ...수열 최대 길이가 100이엇어.. 나왜bisect쓴거야메모리랑시간만더만이쓰고