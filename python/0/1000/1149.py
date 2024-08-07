import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
li = [[0,0,0]]
for _ in range(n):
    li.append(list(map(int,input().split())))
pn = [[0,0,0] for _ in range(n+1)]

for i in range(n+1):
    if i ==0:continue
    pn[i][0] = min(pn[i - 1][1], pn[i - 1][2]) + li[i][0]
    pn[i][1] = min(pn[i - 1][0], pn[i - 1][2]) + li[i][1]
    pn[i][2] = min(pn[i - 1][0], pn[i - 1][1]) + li[i][2]
print(min(pn[-1]))


#  제출 번호 : 80018959, 메모리 : 31120, 시간 : 44