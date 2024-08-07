import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
a = [0] * 2000001 
for _ in range(N):
    b = int(input())
    a[b + 1000000] += 1  
for i in range(2000001):
    if a[i] > 0:
        print(f"{i - 1000000}\n" * a[i])


#  제출 번호 : 79658507, 메모리 : 46744, 시간 : 1072