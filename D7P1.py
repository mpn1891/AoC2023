from enum import Enum

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
    'J': 11,
    'Q': 12,
    'K': 13
}

array = []


# def count_repeat(numbers):
#     count = []
#     hand_type = 1
#     pair_count = 0
#     for i in range(0, len(numbers)):
#         count.append([1, card_dict.get(numbers[i])])
#         for j in range(0, len(numbers)):
#             if i == j:
#                 continue
#             else:
#                 if numbers[i] == numbers[j]:
#                     count[i][0] += 1
#
#     for k in range(len(numbers) - 1, -1, -1):
#         if count[k] in count[:k]:
#             del count[k]
#         else:
#             if hand_type < count[k][0]:
#                 hand_type = count[k][0]
#             if count[k][0] == 2:
#                 pair_count += 1
#
#     if hand_type == 3 and len(count) == 2:
#         hand_type = 3.5
#     if pair_count == 2:
#         hand_type = 2.5
#
#     return hand_type
def count_repeat(numbers):
    count = []
    hand_type = 0
    pair_count = 0
    for i in range(len(numbers)):
        count.append([1, card_dict.get(numbers[i])])
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                count[i][0] += 1

    # Remove duplicates based on card ranks
    unique_count = []
    for c in count:
        if c not in unique_count:
            unique_count.append(c)

    # Determine hand type based on unique_count
    for c in unique_count:
        if hand_type < c[0]:
            hand_type = c[0]
        if c[0] == 2:
            pair_count += 1

    if hand_type == 3 and len(unique_count) == 2:
        hand_type = 3.5  # Full House
    if pair_count == 2:
        hand_type = 2.5  # Two Pairs

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
            # print(lst[j][1], lst[j+1][1])
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
    for i in range(0, len(array)):
        array_ranked_hands.append([i, count_repeat(array[i][0])])
    array_ranked_hands.sort(key=lambda x: x[1], reverse=True)

    bubble_sort(array_ranked_hands)

    print(array_ranked_hands)
    for j in range(len(array_ranked_hands)):
        print(array[array_ranked_hands[j][0]][0],array_ranked_hands[j][1])
    score = 0
    total_hands = len(array_ranked_hands)
    for l in range(0, total_hands):
        print(score, ((total_hands - l), int(array[array_ranked_hands[l][0]][1])), array_ranked_hands[l][0])
        score = score + ((total_hands - l) * int(array[array_ranked_hands[l][0]][1]))

    print(score)


if __name__ == "__main__":
    main()
