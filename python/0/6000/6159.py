import sys
input = lambda: sys.stdin.readline().rstrip()

n,s = map(int,input().split())
num = 0
li = [int(input()) for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if li[i]+li[j] <= s:
            num+=1

print(num)


# 제출 번호 : 82952991,  메모리 : 110532,  시간 : 1380  With Pypy3