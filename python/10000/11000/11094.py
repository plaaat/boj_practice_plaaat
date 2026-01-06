import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    wo = input()
    if wo[:10] == 'Simon says':
        print(wo[10:])

# 제출 번호 : 101392340, 메모리: : 32412, 시간 : 32