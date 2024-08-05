import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = sorted([int(input()) for _ in range(n)])

a = 1 
b = li[-1]

while a <= b:
    m = (a + b) // 2
    c = 0
    for num in li:
        c += num // m
    if c >= k:
        a = m+1
        des = m
    else:
        b = m-1

print(des)#  ���� ��ȣ : 79653800, �޸� : 31120, �ð� : 84