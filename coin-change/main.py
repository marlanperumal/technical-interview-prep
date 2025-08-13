def make_change_greedy(denominations: list[int], amount: int) -> int:
    sorted_denominations = reversed(sorted(denominations))

    num_coins = 0
    for i in sorted_denominations:
        n = amount // i
        c = amount % i

        amount -= n * i
        num_coins += n

        if c == 0:
            return num_coins

    return -1


if __name__ == "__main__":
    print(make_change_greedy([1, 2, 5], 8))
    print(make_change_greedy([1, 2, 5], 18))
    print(make_change_greedy([1, 2, 5, 7], 10))
