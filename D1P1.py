def main():
    array = []
    temp_nums = []
    numbers = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D1.txt", "r") as f:
        for val in f.read().splitlines():
            array.append(val)

    for s in array:
        temp_nums.clear()
        for char in s:
            if char.isdigit():
                print(char)
                temp_nums.append(char)
        print(temp_nums)
        temp_first = temp_nums[0]
        temp_last = temp_nums[len(temp_nums) - 1]
        temp_string = temp_first + temp_last
        number = int(temp_string)

        numbers.append(number)
    answer = 0
    for x in numbers:
        answer += x
    print(answer)


if __name__ == "__main__":
    main()
