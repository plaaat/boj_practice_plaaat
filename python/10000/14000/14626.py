import sys
input = lambda: sys.stdin.readline().rstrip()

mul = 1
wo = input()
n = 0
m = int(wo[-1])
for i in range(12):
    if wo[i] == '*':
        if i % 2:
            mul = 3
    else:
        n += int(wo[i]) * (3 if i % 2 else 1)

for i in range(11):
    if (n + i * mul) % 10 == (10 - m) % 10:
        print(i)
        break

# 제출 번호 : 101218745, 메모리 : 32412, 시간 : 36
