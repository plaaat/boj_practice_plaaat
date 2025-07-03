import sys
input = lambda: sys.stdin.readline().rstrip()

alp = set(chr(i) for i in range(97,123))
while True:
    wo = input()
    if wo == '*':
        break
    wos = set(wo)
    if ' ' in wos:
        wos.remove(' ')
    wos = len(alp - wos)
    if wos == 0:
        print('Y')
    else:
        print('N')

# 제출 번호 : 95870098, 메모리 : 32412, 시간 : 32