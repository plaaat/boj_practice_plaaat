import sys
from math import comb
input = lambda: sys.stdin.readline().rstrip()

m = int(input())
li = list(map(int, input().split()))
k = int(input())
print(sum(comb(i,k) for i in li)/comb(sum(li),k))

# 제출번호 : 84791538, 메모리 : 33372, 시간 : 36
