import sys
input = sys.stdin.readline
m, n = map(int, input().split())
for i in range(m, n + 1):
    if i == 1:
        continue
    a = True
    for j in range(2, int(i**(1/2) + 1)):
        if i % j == 0:
            a = False
            break
    if a:
        print(i)#  ���� ��ȣ : 79654116, �޸� : 31120, �ð� : 5320