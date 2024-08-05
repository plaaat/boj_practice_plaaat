li = ['Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna tell a lie and hurt you','Never gonna say goodbye','Never gonna stop']
t = int(input())
for _ in range(t):
    wo = input()
    if not wo in li:
        print('Yes')
        break
else:
    print('No')#  제출 번호 : 80438839, 메모리 : 31120, 시간 : 32