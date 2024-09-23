import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = b = c = 0
for _ in range(n):
    x,y = map(int,input().split())
    a += x
    b += y
    c += x*y

print(a*b-c)

# 제출 번호 : 84230227,  메모리 : 31252,  시간 : 316