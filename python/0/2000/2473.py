import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = list(map(int,input().split()))

nli.sort()

resn = float('inf')
a,b,c = 0,0,0

for i in range(n-2):
    if resn == 0:
        break
    left, right = i+1, n-1
    while left < right:
        tn = nli[i] + nli[left] + nli[right]
        if abs(tn) < resn:
            resn = abs(tn)
            a = nli[i]
            b = nli[left]
            c = nli[right]
            if resn == 0:
                break
        if tn < 0:
            left += 1
        else:
            right -= 1

print(a,b,c)

# 제출 번호 : 101913678, 메모리 : 110760, 시간 : 140 By.pypy3