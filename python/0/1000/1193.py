import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
x = 0
st = 0

while x < n:
    st += 1
    x += st

t = x - n

if st % 2:
    left = t + 1
    right = st - t
else:
    left = st - t
    right = t + 1
    
print(f'{left}/{right}')

# 제출 번호 : 101823091, 메모리 : 32412, 시간 : 36