def max_matching_cards(N, M, K):
    O_front = M
    O_back = K
    X_front = N - M
    X_back = N - K

    O_match = min(O_front, O_back)
    X_match = min(X_front, X_back)

    return O_match + X_match

N, M, K = map(int, input().split())
print(max_matching_cards(N, M, K))
#  ���� ��ȣ : 80439116, �޸� : 31120, �ð� : 36