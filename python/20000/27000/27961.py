import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
wo = list(input())

lc, rc = n//2, n//2

for w in wo:
    if w == '(':
        lc -= 1
    elif w == ')':
        rc -= 1
    
for i in range(len(wo)):
    if wo[i] == 'G':
        if lc > 0:
            wo[i] ='('
            lc -= 1
        else:
            wo[i] = ')'
print(*wo,sep='')

# 제출 번호 : 96369671, 메모리 : 32412, 시간 : 36