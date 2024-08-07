import sys
input = sys.stdin.readline

def bfs(x,y):
    for a,b in d:
        tx=x; ty=y
        for i in range(7):
            tx+=a; ty+=b
            if tx>=8 or tx<0 or ty>=8 or ty<0:
                break
            if li[tx][ty] == '*':
                return 1
    

li = [list(input().rstrip()) for _ in range(8)]
d = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
cnt = 0
for i in range(8):
    for j in range(8):
        if li[i][j]=='*':
            cnt+=1
            if bfs(i,j):
                print('invalid')
                exit(0)
print('valid' if cnt==8 else 'invalid')


#  제출 번호 : 82137954, 메모리 : 31120, 시간 : 40