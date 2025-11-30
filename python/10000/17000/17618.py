import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
res = 0

for i in range(1, n + 1):
    ni = i
    sn = 0
    while ni:
        sn += ni % 10
        ni //= 10
    
    if i % sn == 0:
        res += 1

print(res)

# 제출 번호 : 99574439, 메모리 : 109544, 시간 : 528