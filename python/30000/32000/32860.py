import sys
input = lambda: sys.stdin.readline().rstrip()

res,m = input().split()
m = int(m)
if m < 27:
    res += chr(64 + m)
else:
    if m % 26 == 0:
        res += chr(95 + m // 26)
        res += 'z'
    else:
        res += chr(96 + m // 26)
        res += chr(96 + m % 26)

print('SN',res)

# 제출 번호 : 97183131, 메모리 : 32412, 시간 : 44