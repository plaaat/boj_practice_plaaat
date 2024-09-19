import sys
input = lambda: sys.stdin.readline().rstrip()

d = [1,2,3,4,5]
li = list(map(int,input().split()))
while li != d:
    for i in range(4):
        if li[i] > li[i+1]:
            li[i+1],li[i] = li[i],li[i+1]
            print(*li)
            
# 제출 번호 : 83740210 메모리 : 31120,  시간 : 32