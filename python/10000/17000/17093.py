import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

nli = [tuple(map(int,input().split())) for _ in range(n)]
mli = [tuple(map(int,input().split())) for _ in range(m)]
mn = -1

for mx,my in mli:
    for nx,ny in nli:
        mn = max(mn,(mx-nx)**2+(my-ny)**2)

print(mn)

# 제출 번호 : 96706524, 메모리 : 33432, 시간 : 436