from collections import defaultdict


def main():
    array = []
    points = 0

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D4.txt", "r") as f:
        for val in f.read().split('\n'):
            array.append(val)

    # Parse every line individually. Each time creating a new dictionary lookup for the winning and normal nums
    for line in array:
        winning = defaultdict(list)
        nums = defaultdict(list)
        temp = line.split()

        # Sets the starting points for winning and normal numbers
        win_start = 2
        your_nums_start = temp.index('|') + 1

        # adds winning to dict
        for j in range(win_start, your_nums_start):
            winning[j-win_start].append(temp[j])

        # adds normal to dict
        for k in range (your_nums_start, len(temp)):
            nums[k-your_nums_start].append(temp[k])

        # counts winners and calculates points
        counter = 0
        for num in nums.values():
            if num in winning.values():
                counter += 1
        if counter > 0:
            points = points + 2**(counter-1)

    print(points)


if __name__ == "__main__":
    main()
