import math

K = input().strip()

p = ''
a, b = 0, 0
o = ''

for i in range(len(K)):
    if p.isdigit() and not K[i].isdigit():
        o = K[i]
        a = int(K[:i], 8)
        b = int(K[i+1:], 8)
    p = K[i]

if o == '/' and b == 0:
    print('invalid')
    exit(0)

res = oct(math.floor(eval(str(a) + o + str(b))))
if res[0] == '-':
    print('-' + res[3:])
else:
    print(res[2:])



#  제출 번호 : 82138742, 메모리 : 33240, 시간 : 44