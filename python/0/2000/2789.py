import sys
input = lambda: sys.stdin.readline().rstrip()

wo = input()
ans = ''
uni = set('CAMBRIDGE')

for w in wo:
    if not w in uni:
        ans += w

print(ans)

# 제출 번호 : 101215969, 메모리 : 32412, 시간 : 36