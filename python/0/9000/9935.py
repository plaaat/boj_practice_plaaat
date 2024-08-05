import sys
input = lambda:sys.stdin.readline().rstrip()

wo = input()
bomb = input()
tem = len(bomb)
stack = []
for i in wo:
    stack.append(i)
    if len(stack)>=tem and ''.join(stack[-tem:]) == bomb:
        del stack[-tem:]
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))#  제출 번호 : 80384003, 메모리 : 42300, 시간 : 708