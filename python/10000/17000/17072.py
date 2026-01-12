import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
res = [[''] * m for _ in range(n)]

for i in range(n):
    nli = list(map(int, input().split()))
    for j in range(0, 3*m, 3):
        x = nli[j] * 2126 + nli[j+1] * 7152 + nli[j+2] * 722
        j = j // 3
        if x < 510000:
            res[i][j] = '#'
        elif x < 1020000:
            res[i][j] = 'o'
        elif x < 1530000:
            res[i][j] = '+'
        elif x < 2040000:
            res[i][j] = '-'
        else:
            res[i][j] = '.'

for r in res:
    print(*r, sep='')

# 제출 번호 : 101821847, 메모리 : 32892, 시간 : 204