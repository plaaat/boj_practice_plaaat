import sys

def v(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return 'NO'
            stack.pop()
    return 'YES' if not stack and s[0] != ')' and s[-1] != '(' else 'NO'

i = sys.stdin.readline

for _ in range(int(i().rstrip('\n'))):
    a = i().rstrip('\n')
    print(v(a))
#  제출 번호 : 79654495, 메모리 : 31120, 시간 : 36