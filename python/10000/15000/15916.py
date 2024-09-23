import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
k = int(input())
tf1 = tf2 = False

for i in range(n):
    te = (i + 1) * k
    if li[i] > te:
        tf1 = True
    elif li[i] < te:
        tf2 = True
    else:
        tf1 = tf2 = True
        break
if tf1 and tf2:
    print('T')
else:print('F')

# 제출 번호 : 84223611,  메모리 : 42036,  시간 : 84