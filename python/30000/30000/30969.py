import sys
input = sys.stdin.readline

t = int(input())
li = [0] * 1002
for _ in range(t):
    a,b = input().split()
    if a == 'jinju':
        jin = int(b)
    else:
        li[(int(b) if int(b) < 1001 else 1001)] += 1
print(jin)
print(sum(li[jin+1:]))


#  제출 번호 : 86467749, 메모리 : 112904, 시간 : 2116