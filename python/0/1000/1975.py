import sys
input = sys.stdin.readline

T = int(input())
results = []

for i in range(1, T + 1):
    N = int(input())
    total_zeros = 0
    
    for base in range(2, N + 1):
        count = 0
        current = N
        while current % base == 0:
            current //= base
            count += 1
        total_zeros += count
    
    results.append(total_zeros)
print(*results,sep='\n')
#  제출 번호 : 80440058, 메모리 : 116140, 시간 : 776