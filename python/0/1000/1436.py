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
    break#  ���� ��ȣ : 79654028, �޸� : 31120, �ð� : 752