import sys
input = sys.stdin.readline

n = int(input())
x,s = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]

for i in li:
    if i[0] <= x and i[1] > s:
        print('YES')
        break
else:
    print('NO') #  제출 번호 : 81887149, 메모리 : 31120, 시간 : 48