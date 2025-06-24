import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
ali = list(map(int,input().split()))
fla = [True] * (n+1)

q = int(input())
res = sum(ali)
print(res)

for _ in range(q):
    inp1 = list(map(int,input().split()))
    a = inp1[1] - 1
    if inp1[0] == 1:
        b = inp1[2]
        if fla[a]:
            res -= ali[a]
            res += b
        ali[a] = b        
    else:
        if fla[a]:
            fla[a] = False
            res -= ali[a]
        else:
            fla[a] = True
            res += ali[a]
    print(res)