

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

def count_repeat(numbers):
    count = []
    hand_type = 0
    pair_count = 0
    j_count = 0
    for i in range(5):
        count.append([1, card_dict.get(numbers[i])])
        if card_dict.get(numbers[i]) == 1:
            j_count += 1
        for j in range(5):
            if i != j and numbers[i] == numbers[j]:
                count[i][0] += 1

    # Remove duplicates based on card ranks
    unique_count = []
    for c in count:

        if c not in unique_count and c[1] != 1:
            unique_count.append(c)

    # Determine hand type based on unique_count

    for c in unique_count:
        if hand_type < c[0]:
            hand_type = c[0]
        if c[0] == 2:
            pair_count += 1
    if hand_type == 3 and pair_count:
        hand_type = 3.5  # Full House
    if pair_count == 2 and hand_type < 2.5:
        hand_type = 2.5  # Two Pairs
    hand_type += j_count
    return hand_type


def bubble_sort(lst):
    lst_len = len(lst)
    # Traverse through all elements in the array
    for i in range(lst_len):
        # Flag to check if any swapping happens
        swapped = False
        # Last i elements are already sorted, so reduce the range
        for j in range(0, lst_len - i - 1):
            # Swap if the element found is greater than the next element

            if lst[j][1] < lst[j + 1][1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
            elif lst[j][1] == lst[j + 1][1]:
                for k in range(5):
                    if card_dict.get(array[lst[j][0]][0][k]) < card_dict.get(array[lst[j + 1][0]][0][k]):
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                        swapped = True
                        break
                    elif card_dict.get(array[lst[j][0]][0][k]) > card_dict.get(array[lst[j + 1][0]][0][k]):
                        # No need to swap, this jth element is greater
                        break
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break


def main():
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D7.txt", "r") as f:
        for line in f.read().splitlines():
            hand, bet = line.split()
            array.append([hand, bet])

    array_ranked_hands = []
    num_hands = len(array)
    for i in range(0, num_hands):
        array_ranked_hands.append([i, count_repeat(array[i][0])])

    array_ranked_hands.sort(key=lambda x: x[1], reverse=True)

    bubble_sort(array_ranked_hands)

    score = 0
    for l in range(0, num_hands):
        score = score + ((num_hands - l) * int(array[array_ranked_hands[l][0]][1]))

    print(score)


if __name__ == "__main__":
    st = time.time()
    main()
    print("----%.2f----" % (time.time() - st))
