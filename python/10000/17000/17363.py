import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
orgli = [input() for _ in range(n)]
resli = [[''] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        wo = orgli[i][j]
        match wo:
            case '-':
                wo = '|'
            case '|':
                wo = '-'
            case '/':
                wo = '\\'
            case '\\':
                wo = '/'
            case '^':
                wo = '<'
            case '<':
                wo = 'v'
            case 'v':
                wo = '>'
            case '>':
                wo = '^'
            case _:
                pass
        resli[m-j-1][i] = wo

for res in resli:
    print(*res, sep='')

# 제출 번호 : 101590849, 메모리 : 32412, 시간 : 40