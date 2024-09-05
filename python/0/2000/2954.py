import sys
input = lambda: sys.stdin.readline().rstrip()

mo = set(['a','e','i','o','u'])
wo = input().split()

for w in wo:
    t = 0
    for i in w:
        if t > 0:
            t -= 1
            continue
        if i in mo:
            t = 2
        print(i,end='')
    print(' ',end='')

# 제출 번호 : 83458056,  메모리 : 31120,  시간 : 32