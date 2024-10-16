def count_repeat(numbers):
    count = {}
    hand_type = 0
    pair_count = 0

    # Count occurrences of each card using a dictionary (O(n))
    for card in numbers:
        count[card] = count.get(card, 0) + 1

    # Determine hand type based on counts
    for c in count.values():
        if hand_type < c:
            hand_type = c
        if c == 2:
            pair_count += 1

    if hand_type == 3 and len(count) == 2:
        hand_type = 3.5  # Full House
    if pair_count == 2:
        hand_type = 2.5  # Two Pairs

    return hand_type

import time

card_dict = {
    'A': 14,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13
}

array = []
def sort_hands(array_ranked_hands):
    # Sort by hand rank first, then by card rank as tiebreaker
    array_ranked_hands.sort(key=lambda x: (x[1], [card_dict[card] for card in array[x[0]][0]]), reverse=True)


def main():
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D7.txt", "r") as f:
        for line in f.read().splitlines():
            hand, bet = line.split()
            array.append([hand, bet])

    array_ranked_hands = []
    for i in range(len(array)):
        rank = count_repeat(array[i][0])
        array_ranked_hands.append([i, rank])

    # Sort hands efficiently
    sort_hands(array_ranked_hands)

    score = 0
    total_hands = len(array_ranked_hands)
    for l in range(total_hands):
        score += (total_hands - l) * int(array[array_ranked_hands[l][0]][1])

    print(score)


if __name__ == "__main__":
    st = time.time()
    main()
    print("----%.2f----" % (time.time() - st))
