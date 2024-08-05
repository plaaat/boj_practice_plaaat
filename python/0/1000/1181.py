import sys
input = sys.stdin.readline
a = int(input())
l = {}
for _ in range(a):
    b = input().strip()
    if b not in l:
        l[b] = len(b)
c = sorted(l.keys(), key=lambda x: (len(x), x))
for i in c:
    print(i)#  제출 번호 : 79658497, 메모리 : 34756, 시간 : 88