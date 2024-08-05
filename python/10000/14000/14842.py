import sys
input = lambda:sys.stdin.readline().rstrip()
a,b,n = map(int,input().split())
if n % 2 == 0:
    result = (n - 2) / 4
else:
    result = (n - 1) * (n - 1) / (4 * n)
result *= 2 * b
print(result)#  제출 번호 : 81597313, 메모리 : 31120, 시간 : 40