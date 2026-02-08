import sys
input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left as bil

n = int(input())
li = []
ali = []
aset = set()

for _ in range(n):
    a,b = map(int,input().split())
    aset.add(a)
    ali.append((a,b))

ali.sort()
li.append(ali[0][1])
rec = [None] * (n + 1)
rec[0] = (1,ali[0][0])

for i in range(1,n):
    a,b = ali[i]
    if li[-1] >= b:
        idx = bil(li,b)
        li[idx] = b
        rec[i] = (idx+1,a)
    else:
        li.append(b)
        rec[i] = (len(li),a)

tarl = len(li)
for i in range(n-1,-1,-1):
    if rec[i] and rec[i][0] == tarl:
        aset.remove((rec[i][1]))
        tarl -= 1

print(len(aset))
print(*sorted(aset),sep='\n')

# 제출 번호 : 102745953, 메모리 : 60572, 시간 : 280