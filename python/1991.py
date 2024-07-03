import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    pa, l, r = input().split()
    dic[pa] = [l,r]

def pre(tem):
    if tem == '.':
        return
    print(tem,end='')
    pre(dic[tem][0])
    pre(dic[tem][1])

def mid(tem):
    if tem == '.':
        return
    mid(dic[tem][0])
    print(tem,end='')
    mid(dic[tem][1])

def fin(tem):
    if tem == '.':
        return
    fin(dic[tem][0])
    fin(dic[tem][1])
    print(tem, end='')

pre('A')
print('')
mid('A')
print('')
fin('A')