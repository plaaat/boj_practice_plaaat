def s(a, b, v):
    r = v - a
    d = a - b
    n = r // d
    if r % d != 0:
        n += 1
    return n + 1

a, b, v = map(int, input().split())
print(s(a, b, v))#  ���� ��ȣ : 79658481, �޸� : 108080, �ð� : 112