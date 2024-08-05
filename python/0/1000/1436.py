import sys
input = sys.stdin.readline

a = int(input())
count = 0
number = 0
while True:
  number+=1
  e = str(number)
  if '666' in e:
    count+=1
  if count == a:
    print(number)
    break#  제출 번호 : 79654028, 메모리 : 31120, 시간 : 752