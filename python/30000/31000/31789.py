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
    print('NO') #  ���� ��ȣ : 81887149, �޸� : 31120, �ð� : 48