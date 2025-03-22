import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = list(map(int,input().split()))
mn = sum(nli) // n
an1 = 0
an2 = 0

for i in nli:
    if i - 1 > mn: an1 += (i - 1 - mn)
    if i < mn: an2 += (mn - i)
print(max(an1,an2))

# 제출 번호 : 90869475, 메모리 : 129768, 시간 : 464