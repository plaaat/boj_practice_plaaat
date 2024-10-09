import sys
input = lambda: sys.stdin.readline().strip()

n,m = map(int,input().split())
li = [0] * n
for i in range(m):
    x,y = map(int,input().split())
    li[x-1:y] = [i+1] * (y-x+1)

print(2 ** (len(set(li) - {0})))

# 제출 번호 : 84876255, 메모리 : 31120, 시간 : 36