from collections import defaultdict


def main():
    array = []
    num_cards = []
    points = 0

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D4.txt", "r") as f:
        for val in f.read().split('\n'):
            array.append(val)

    # Creates a base list of card counts start with 1 of everything
    for x in array:
        num_cards.append(1)

    # tracker for which card we are currently looking at
    cur_card = 0
    # Parse every line individually. Each time creating a new dictionary lookup for the winning and normal nums
    for line in array:
        winning = defaultdict(list)
        nums = defaultdict(list)
        temp = line.split(' ')

        # removes the '' element from numbers that only have 1 digit in input
        for i, element in enumerate(temp):
            if element == '':
                temp.pop(i)

        # Sets the starting points for winning and normal numbers
        win_start = 2
        your_nums_start = temp.index('|') + 1

        # adds winning to dict
        for j in range(win_start, your_nums_start):
            winning[j-win_start].append(temp[j])

        # adds normal to dict
        for k in range(your_nums_start, len(temp)):
            nums[k-your_nums_start].append(temp[k])

        # counts winners and calculates how many cards to add.
        counter = 0
        for num in nums.values():
            if num in winning.values():
                counter += 1
        if counter > 0:
            for y in range(1, counter+1):
                # This takes into account how many cards we already have that will do this, hence the multiply
                num_cards[cur_card+y] += 1*num_cards[cur_card]
        # increments to next card for knowing where we are in the card array
        cur_card += 1

    p2_ans = 0
    for count in num_cards:
        p2_ans += count
    print(p2_ans)


if __name__ == "__main__":
    main()
