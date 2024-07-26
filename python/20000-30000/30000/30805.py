import sys
import itertools
input = lambda:sys.stdin.readline().rstrip()

di = {}
n = int(input())
nl = list(map(int,input().split()))
m = int(input())
ml = list(map(int,input().split()))
if n<m:li = itertools.dropwhile(lambda x: x in ml,nl)
else:li = itertools.dropwhile(lambda x: x in nl,ml)
li = itertools.product(li)
print(li)