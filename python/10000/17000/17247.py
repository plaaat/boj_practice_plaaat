import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
flag = False
x2,y2 = -1,-1
for i in range(n):
    tli = list(map(int, input().split()))
    for j in range(m):
        if tli[j] == 1 and not flag:
            x1,y1 = i,j
            flag = True
            break
        elif tli[j] == 1 and flag:
            x2,y2 = i,j
            break
    if x2 != -1:
        break

print(abs(x1-x2) + abs(y1-y2))

# 제출 번호 : 95084827, 메모리 : 32412, 시간 : 184