import sys

wos = sys.stdin.readlines()

for wo in wos:
    wo = wo.rstrip()
    while True:
            for i in range(len(wo) - 2):
                if wo[i] == 'B' and wo[i+1] == 'U' and wo[i+2] == 'G':
                    wo = wo[:i] + wo[i+3:]
                    break
            else:
                break
    print(wo)

# 제출 번호 : 96930710, 메모리 : 32412, 시간 : 36