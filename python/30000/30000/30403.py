import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
up = set('ROYGBIV')
lo = set('roygbiv')

for w in input():
    up.discard(w)
    lo.discard(w)

if not up and not lo:
    print('YeS')
elif not up:
    print('YES')
elif not lo:
    print('yes')
else:
    print('NO!')

# 제출 번호 : 102597839, 메모리 : 32412, 시간 : 32