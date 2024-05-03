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
print("-----------------------------")

def construct_rectangle(area: int) -> list[int]:
    sqrt_area = int(area ** 0.5)
    for width in range(sqrt_area, 0, -1):
        if area % width == 0:
            height = area // width
            return [height, width]


print(construct_rectangle(37)) 
print(construct_rectangle(49))
print(construct_rectangle(4))
print(construct_rectangle(35))