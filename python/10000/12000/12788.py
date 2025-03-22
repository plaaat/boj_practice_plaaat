import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m,k = map(int,input().split())
nums = m * k

a = list(map(int,input().split()))
a.sort(reverse=True)
res = 0
for i in a:
    nums -= i
    res += 1
    if nums <= 0:
        break
else:
    res = 'STRESS'

print(res)

# 제출번호 : 91582199, 메모리 : 32412, 시간 : 36