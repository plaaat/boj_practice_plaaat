import sys
input = lambda: sys.stdin.readline().rstrip()

w = input()
count = 0
num = 0

for i in range(1,len(w)):
    if w[i] == w[i-1]:
        if w[i] == '(':
            count += 1
        else:
            num += count

print(num)


# 제출 번호 : 82412201  메모리 : 31120  시간 : 48