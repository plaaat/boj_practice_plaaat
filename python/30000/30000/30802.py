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

print(b,n-(b*p))#  제출 번호 : 79646247, 메모리 : 31120, 시간 : 36