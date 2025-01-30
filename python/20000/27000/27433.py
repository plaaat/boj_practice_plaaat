import sys
input = sys.stdin.readline

n = int(input())
m = 1
for i in range(1,n+1):
    m *= i
print(m)


#  제출 번호 : 89170719, 메모리 : 32412, 시간 : 36