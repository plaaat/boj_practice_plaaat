import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num = 0
    for _ in range(n):
        num+=0.5
        num*=2
    print(int(num))#  ���� ��ȣ : 81953817, �޸� : 31120, �ð� : 48