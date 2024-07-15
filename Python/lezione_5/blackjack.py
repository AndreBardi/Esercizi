def blackjack(hand: list[int]) -> int:
    total_sum: int = sum(hand)
    num_aces: int = hand.count(1) # + hand.count(11)

    while total_sum > 21 and num_aces != 0:
        total_sum -= 10
        num_aces -= 1

    return total_sum

print(blackjack([2, 3, 5])) #10
print(blackjack([11, 5, 5])) #21
print(blackjack([1, 10, 11])) #12
print(blackjack([1, 10, 5])) #16