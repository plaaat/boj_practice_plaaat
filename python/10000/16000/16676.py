import sys
input = lambda: sys.stdin.readline().rstrip()

wo = input()
card = '1' * len(wo)

if len(wo) == 1:
    print(1)
else:
    if int(wo) >= int(card):
        print(len(wo))
    else:
        print(len(wo) - 1)