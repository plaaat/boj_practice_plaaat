import sys

N = int(sys.stdin.readline())
count = [0] * 10001 

for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for s in range(count[i]):
            print(i)



#  제출 번호 : 79658606, 메모리 : 126180, 시간 : 3012