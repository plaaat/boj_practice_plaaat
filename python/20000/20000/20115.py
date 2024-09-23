import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
li.sort()
print(sum(li)/2+(li[-1]/2))

# 제출 번호 : 84165701,  메모리 : 42036,  시간 : 76
