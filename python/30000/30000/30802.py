import sys

input = lambda:sys.stdin.readline().rstrip()

n = int(input())

li = list(map(int,input().split()))

t,p = map(int,input().split())

a = 0

for i in li:

    a+=(i+t-1)//t

print(a)

b = n//p

print(b,n-(b*p))#  ���� ��ȣ : 79646247, �޸� : 31120, �ð� : 36