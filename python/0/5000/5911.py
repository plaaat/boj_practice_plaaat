import sys
input = lambda: sys.stdin.readline().rstrip()

n,b = map(int,input().split())
li = [tuple(map(int,input().split())) for _ in range(n)]
mn = 0
mv = 0

for i in range(n):
    pn = []
    tn = 0
    for j in range(n):
        if i == j:
            pn.append((li[j][0]//2) + li[j][1])
        else:
            pn.append(li[j][0] + li[j][1])
    pn.sort()
    val = 0
    for i in pn:
        tn += i
        if tn > b:break
        val += 1
    mv = max(mv,val)
print(mv)

# 제출 번호 : 85576051, 메모리 : 31120, 시간 : 400