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
    print(i)#  ���� ��ȣ : 79658497, �޸� : 34756, �ð� : 88