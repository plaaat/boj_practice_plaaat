import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = []
for _ in range(n+1):
    t,st = input().split()
    tt,mm = map(int,t.split(':'))
    t = tt * 60 + mm
    if st[0] == 't':
        st = 'a'
    li.append((t,st))

stf = False
li.sort()
dt,dm = map(int,input().split(':'))
dd = dt * 60 + dm

res = 0
for lt,lst in li:
    if lst == 'a':
        stf = True
        continue
    if stf and lt >= dd:
        res += 1
print(res)

# 제출 번호 : 94598688, 메모리 : 32412, 시간 : 44