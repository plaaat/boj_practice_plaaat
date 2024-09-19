li = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
wo = input()
num = 0
for i in wo:
    i = ord(i) - ord("A")
    num += li[i]

num %= 10
if num % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")


#  제출 번호 : 82039885, 메모리 : 33076, 시간 : 252
