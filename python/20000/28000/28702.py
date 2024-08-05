for i in range(3):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + (3-i)

if n%15==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)#  제출 번호 : 79686116, 메모리 : 31120, 시간 : 40