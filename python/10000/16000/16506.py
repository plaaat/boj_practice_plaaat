import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dic = {
    'ADD':'0000',
    'SUB':'0001',
    'MOV':'0010',
    'AND':'0011',
    'OR':'0100',
    'NOT':'0101',
    'MULT':'0110',
    'LSFTL':'0111',
    'LSFTR':'1000',
    'ASFTR':'1001',
    'RL':'1010',
    'RR':'1011'
}
for _ in range(n):
    a,b,c,d, = input().split()
    b,c,d = map(int,(b,c,d))
    ctf = 0
    if not a in dic:
        print(dic[a.rstrip('C')],end='')
        print(1,end='')
        ctf = 1
    else:
        print(dic[a],end='')
        print(0,end='')
    print(0,end='')
    print(bin(int(b))[2:].zfill(3),end='')
    print(bin(int(c))[2:].zfill(3),end='')
    if not ctf:
        print(bin(int(d))[2:].zfill(3),end='')
        print(0)
    else:
        print(bin(int(d))[2:].zfill(4))
    
# 제출 번호 : 85003219, 메모리 : 31120, 시간 : 32