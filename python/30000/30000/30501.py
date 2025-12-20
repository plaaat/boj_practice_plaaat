import sys 
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    wo = input()
    if 'S' in wo:
        print(wo)
        break

# 제출 번호 : 101215873, 메모리 : 32412, 시간 : 32
