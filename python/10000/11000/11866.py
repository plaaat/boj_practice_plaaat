import sys
input = sys.stdin.readline
n, k = map(int, input().split())
r = []
p = list(range(1, n + 1))
i = 0

while p:
    i = (i + k - 1) % len(p)
    r.append(p.pop(i))

print("<", end="")
print(*r, sep=", ", end="")
print(">")#  ���� ��ȣ : 79654450, �޸� : 109108, �ð� : 116