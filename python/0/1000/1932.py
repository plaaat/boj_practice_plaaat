import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            li[i][0] += li[i-1][0]
        elif j == i:
            li[i][j] += li[i-1][j-1]
        else:
            li[i][j] += max(li[i-1][j-1],li[i-1][j])
print(max(li[-1]))#  ���� ��ȣ : 80302647, �޸� : 35612, �ð� : 116