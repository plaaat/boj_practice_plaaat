import sys
input = lambda: sys.stdin.readline().rstrip()

wo = input()
n = int(input())
ans = 0

for _ in range(n):
    tw = input()
    tw = tw + tw + tw
    if wo in tw:
        ans += 1

print(ans)

# 제출 번호 : 101217104, 메모리 : 32412, 시간 : 32