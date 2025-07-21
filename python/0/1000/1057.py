import sys
input = lambda: sys.stdin.readline().rstrip()

n,k,i = map(int,input().split())

ans = 0
half = lambda x: x // 2 + (x % 2)

while k != i:
    k = half(k)
    i = half(i)
    ans += 1
print(ans)

# 제출 번호 : 96340307, 메모리 : 32412, 시간 : 48