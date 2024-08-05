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
print(p[s:e+1])#  제출 번호 : 79641491, 메모리 : 34056, 시간 : 276