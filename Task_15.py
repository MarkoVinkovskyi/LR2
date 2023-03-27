
def find_missing_card(N, Cards):
    expected_sum = (N * (N + 1)) // 2
    actual_sum = sum(Cards)
    return expected_sum - actual_sum

n, *cards = map(int, input().split())
print(find_missing_card(n, cards))