import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

sud = [list(map(int,input())) for _ in range(9)]

xsets = [0] * 9
ysets = [0] * 9
sqsets = [0] * 9
blist = []

for i in range(9):
    for j in range(9):
        if sud[i][j] != 0:
            num = sud[i][j]
            bit = 1 << (num - 1)

            xsets[j] |= bit
            ysets[i] |= bit
            sqsets[(i // 3) * 3 + j // 3] |= bit
        else:
            blist.append((j,i))

def sudoku(idx):
    global sud
    global xsets
    global ysets
    global sqsets

    if idx == len(blist):
        return True
    else:
        x,y = blist[idx]
    avail = xsets[x] | ysets[y] | sqsets[(y//3) * 3 + x//3]
    
    for i in range(9):
        bit = 1 << i
        if not avail & bit:
            xsets[x] |= bit
            ysets[y] |= bit
            sqsets[(y//3) * 3 + x//3] |= bit
            sud[y][x] = i+1
            if sudoku(idx + 1):
                return True
            xsets[x] &= ~bit
            ysets[y] &= ~bit
            sqsets[(y//3) * 3 + x//3] &= ~bit
            sud[y][x] = 0
    return False

sudoku(0)
for s in sud:
    print(*s, sep='')

# 제출 번호 : 101673360, 메모리 : 32412, 시간 : 4776