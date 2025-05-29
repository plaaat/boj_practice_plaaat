import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
li = [int(input()) for _ in range(t)]
li.sort()
res = float('inf')

for i in range(t):
    tli = set([li[j] for j in range(i,min(t,i + 5))])
    xli = set([j for j in range(li[i],li[i]+5)])
    res = min(res,len(xli - tli))
print(res)

# 제출 번호 : 94871355, 메모리 : 32412, 시간 : 32