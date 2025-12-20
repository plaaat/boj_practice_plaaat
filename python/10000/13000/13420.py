import sys
input = lambda: sys.stdin.readline().rstrip()

def calc(x,y,c):
    if c == '*':
        return x*y
    if c == '+':
        return x+y
    if c == '-':
        return x-y
    return x / y

n = int(input())
for _ in range(n):
    wol = input().split()
    if calc(int(wol[0]),int(wol[2]),wol[1]) == int(wol[4]):
        print('correct')
    else:
        print('wrong answer')

# 제출 번호 : 101216435, 메모리 : 32412, 시간 : 40