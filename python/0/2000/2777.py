import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        res = 0
        for i in range(9,1,-1):
            while n % i == 0:
                n //= i
                res += 1
        if n == 1:
            print(res)
        else:
            print(-1)

# 제출 번호 : 94599977, 메모리 : 32412, 시간 : 48