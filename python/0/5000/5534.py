import sys
import re
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
wo =input()
rwo = lambda x: re.compile('[a-z]*'+f'[a-z]{{{x}}}'.join(wo)+'[a-z]*')
pn = 0
for _ in range(n):
    t = input()
    for i in range(len(t)):
        if rwo(i).match(t):
            pn += 1
            break
print(pn)