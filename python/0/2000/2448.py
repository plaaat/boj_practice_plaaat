import sys
input = lambda: sys.stdin.readline().rstrip()

tri1 = [
    "  *  ",
    " * * ",
    "*****"
]

n = int(input())

out = [[' ' for _ in range(2 * n - 1)] for _ in range(n)]
n //= 3

def tri(n,x,y):
    global out

    if n == 1:
        for i in range(3):
            for j in range(5):
               out[y + i][x + j] = tri1[i][j]
    else:
        tri(n//2,x,y+3*n//2)
        tri(n//2,x+3*n//2,y)
        tri(n//2,x+3*n,y+3*n//2)

tri(n,0,0)
for wo in out:
    print(*wo,sep="")