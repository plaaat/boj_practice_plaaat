import sys

input = lambda: sys.stdin.readline().rstrip()

mo = set(['a','e','i','o','u'])
while True:
    wo = input()
    if wo == 'end':
        break
    etf = False
    mot = True
    if len(wo) == 2:
        if wo[0] == wo[1] and wo[0] != 'o' and wo[0] != 'e':
            print(f'<{wo}> is not acceptable.')
        elif not wo[0] in mo and not wo[1] in mo;
            print(f'<{wo}> is not acceptable.')
        else:
            print(f'<{wo}> is acceptable.')
        continue
    
    if len(wo) == 1:
        if wo in mo:
            print(f'<{wo}> is acceptable.')
        else:
            print(f'<{wo}> is not acceptable.')
        continue

    for i in range(len(wo)-2):
        w1,w2,w3 = wo[i],wo[i+1],wo[i+2]
        if w1 == w2 and w1 != 'o' and w1 != 'e':
            etf = True
            break
        elif w2 == w3 and w2 != 'o' and w2 != 'e':
            etf = True
            break
        elif w1 in mo and w2 in mo and w3 in mo:
            etf = True
            break
        elif not w1 in mo and not w2 in mo and not w3 in mo:
            etf = True
            break
        else:
            if w1 in mo or w2 in mo or w3 in mo:
                mot = False
    
    if mot or etf:
        print(f'<{wo}> is not acceptable.')
    else:
        print(f'<{wo}> is acceptable.')


# 제출 번호 : 82856498, 메모리 : 31120, 시간 : 28