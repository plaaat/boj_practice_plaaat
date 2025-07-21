import sys
input = lambda: sys.stdin.readline().rstrip()

m,n = map(int,input().split())

spa = [list(map(int,input().split())) for _ in range(m)]
res = 0

def cl(x,y):
    if x > y:
        return 1
    elif x < y:
        return 2
    else:
        return 3

for i in range(m-1):
    for j in range(i+1,m):
        a = spa[i]
        b = spa[j]
        fl = True
        for x in range(n-1):
            for y in range(x+1,n):
                if cl(a[x],a[y]) != cl(b[x], b[y]):
                    fl = False
                    break
            if not fl:break
        else:
            res += 1

print(res)

# 제출 번호 : 96580784, 메모리 : 32412, 시간 : 100