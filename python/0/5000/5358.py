printer = lambda x: print(x,end='')
while True:
    try:
        wo = input()
        for i in wo:
            if i == 'i':
                printer('e')
            elif i == 'I':
                printer('E')
            elif i == 'e':
                printer('i')
            elif i == 'E':
                printer('I')
            else:
                printer(i)
        print()
    except:
        break
    
# 제출 번호 : 83619802,  메모리 : 31120,  시간 : 32
