import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
li = [int(input()) for _ in range(t)]
li.sort()

print(sum(abs(i+1-li[i]) for i in range(t)))