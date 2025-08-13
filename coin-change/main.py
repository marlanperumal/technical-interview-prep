from functools import cache


def make_change_greedy(denominations: list[int], amount: int) -> int:
    sorted_denominations = sorted(denominations, reverse=True)

    num_coins = 0
    for i in sorted_denominations:
        n = amount // i
        c = amount % i

        amount -= n * i
        num_coins += n

        if c == 0:
            return num_coins

    return -1


def make_change_dp(denominations: list[int], amount: int) -> int:
    @cache
    def make_change(amount: int, value: int = 0) -> int:
        if amount == value:
            return 1

        if value > amount:
            return -1

        change_values = [
            make_change(amount - value, next_value) for next_value in denominations
        ]
        valid_change_values = [i for i in change_values if i > 0]
        if len(valid_change_values) > 0:
            return min(valid_change_values) + (1 if value > 0 else 0)

        return -1

    return make_change(amount)


if __name__ == "__main__":
    print(make_change_greedy([1, 2, 5], 8))
    print(make_change_greedy([1, 2, 5], 18))
    print(make_change_greedy([1, 2, 5, 7], 10))

    print(make_change_dp([1, 2, 5], 8))
    print(make_change_dp([1, 2, 5], 18))
    print(make_change_dp([1, 2, 5, 7], 10))
