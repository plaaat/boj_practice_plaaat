import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
know = list(map(int,input().split()))
knows = know[0]
know = set(know)
