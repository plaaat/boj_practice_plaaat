import sys
input = lambda: sys.stdin.readline().rstrip()

wo = input()
wo = wo.lower()

dic = {
    'northlondo' : 'NLCS',
    'branksomeh' : 'BHA',
    'koreainter' : 'KIS',
    'stjohnsbur' : 'SJA'
}

for i in range(27):
    tw = ''
    for x in wo:
        if ord(x) == 97:
            tw += 'z'
        else:
            tw += chr(ord(x)-1)
    if tw in dic:
        print(dic[tw])
        break
    else:
        wo = tw
        
# 제출 번호 : 84683970, 메모리 : 31120, 시간 : 36