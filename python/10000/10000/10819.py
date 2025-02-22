import sys
from itertools import permutations as pm

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
print(max(sum(abs(i[j] - i[j + 1]) for j in range(n - 1)) for i in pm(list(map(int, input().split())))))

# 제출 번호 : 90432867, 메모리 : 32412, 시간 : 84