import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
res = 0
for i in range(1,10):
    if i <= n:
        res += 1
    for j in range(10):
        a = j - i
        t = i * 10 + j
        while t <= n:
            res += 1
            j += a
            if j < 0 or j > 9:
                break
            t = t * 10 + j

print(res)

# 제출 번호 : 90194617, 메모리 : 32412, 시간 : 40