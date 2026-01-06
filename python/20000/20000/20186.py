import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int, input().split())
nli = list(map(int,input().split()))
nli.sort(reverse=True)
print(sum(nli[:k]) - k * (k-1)//2)

# 제출 번호 : 101594145, 메모리 : 33432, 시간 : 40