import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
print(n * (n-1) // 2)
for i in range(n):print(2 ** i ,end = ' ')
print()
print(n - 1)
li = range(1,n+1)
print(*li,sep=' ')

# 제출 번호 : 85632514, 메모리 : 31252, 시간 : 32
# 아니이건머넌센스도아니고끼야아아아아
# 문제이해를못햇네..