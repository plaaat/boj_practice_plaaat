import sys
input = lambda: sys.stdin.readline().rstrip()

dic = {}
n = int(input())
for _ in range(n):
  a,b = input().split()
  dic[b] = a
p = "?"
wo = input()
for i in wo:
  p+=dic[i]
s,e = map(int,input().split())
print(p[s:e+1])#  ���� ��ȣ : 79641491, �޸� : 34056, �ð� : 276