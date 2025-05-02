import sys
input = lambda: sys.stdin.readline().rstrip()

wli = list(input())
for i in range(10):
    if wli[i] == '@':
        rb = i
    elif wli[i] == '#':
        bo = i
    elif wli[i] == '!':
        bot = i
if rb < bo < bot or rb > bo > bot:
    print(abs(bot - rb) - 1)
else:
    print(-1)

# 제출 번호 : 93842199, 메모리 : 32544, 시간 : 40