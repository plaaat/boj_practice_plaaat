import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
n = 0
li = [int(input()) for _ in range(t)]
mn = -1
for i in range(t):
    i = t-1-i
    if li[i] > mn:
        mn = li[i]
        n+=1
print(n)#  제출 번호 : 81518263, 메모리 : 34972, 시간 : 88