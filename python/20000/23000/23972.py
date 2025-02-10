import sys
input = lambda: sys.stdin.readline().rstrip()

k,n = map(int,input().split())

if n == 1:
    x = -1
else:
    x = (k * n) // (n - 1)
    if (k * n) % (n - 1) != 0:
        x += 1
print(x)

# 제출 번호 : 89607200, 메모리 : 32412, 시간 : 40