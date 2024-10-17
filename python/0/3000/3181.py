import sys
input = lambda: sys.stdin.readline().rstrip()

st = set(['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])
wo = input().split()
print(wo[0][0].capitalize(),end='')
if len(wo) != 1:
    for i in wo[1:]:
        if not i in st:
            print(i[0].capitalize(),end='')
print()

# 제출 번호 : 85263427, 메모리 : 31120, 시간 : 32