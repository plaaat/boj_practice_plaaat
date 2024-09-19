import sys
input = lambda:sys.stdin.readline().strip()

t = int(input())
if t == 1:
    print(1)
else:
    a,b = 1,1
    for _ in range(t-1):
        a,b = a+b+1,a
    print(a % 1000000007)
    
# 제출 번호 : 83568105,  메모리 : 31120,  시간 : 40
