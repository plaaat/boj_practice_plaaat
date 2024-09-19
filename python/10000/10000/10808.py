import sys
input = lambda: sys.stdin.readline().rstrip()

li = [0] * 26
wo = input()
for i in wo:
    li[ord(i)-97] += 1
print(*li,sep=' ')

# 제출 번호 : 83639438, 메모리 : 31120, 시간 : 40
