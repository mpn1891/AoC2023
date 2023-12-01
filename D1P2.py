def main():
    array = []
    spelled_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    from_left = []
    from_right = []
    temp_nums = []
    temp_nums_index = []
    numbers = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D1.txt", "r") as f:
        for val in f.read().splitlines():
            array.append(val)

    for s in array:
        # clearing all working arrays
        from_left.clear()
        from_right.clear()
        temp_nums.clear()
        temp_nums_index.clear()

        # finding left most words and recording index
        for word in spelled_nums:
            pos = s.find(word)
            from_left.append([pos, word])
        # finding right most words and recording index
        for word in spelled_nums:
            pos = s.rfind(word)
            from_right.append([pos, word])

        # finding all literal numbers and recording index
        for index in range(0, len(s)):
            if s[index].isdigit():
                temp_nums.append(s[index])
                temp_nums_index.append(index)

        # finding most left and most right from above information
        # If there was at least one number, we can use that for the first leftmost and rightmost check
        # otherwise we set min to end of string (len), and max to start (0)
        if len(temp_nums_index):
            min_pos = min(temp_nums_index)
            max_pos = max(temp_nums_index)
            temp_first = s[min_pos]
            temp_last = s[max_pos]
        else:
            min_pos = len(s) - 1
            max_pos = 0
        # If there is a word before the first literal number use it
        for i in range(0, len(from_left)):
            if from_left[i][0] != -1 and from_left[i][0] < min_pos:
                min_pos = from_left[i][0]
                temp_first = i + 1
        # If there is a word after the first literal number use it
        for i in range(0, len(from_right)):
            if from_right[i][0] != -1 and from_right[i][0] > max_pos:
                max_pos = from_right[i][0]
                temp_last = i + 1

        temp_string = str(temp_first) + str(temp_last)
        number = int(temp_string)

        numbers.append(number)

    answer = 0
    for x in numbers:
        answer += int(x)
    print(answer)


if __name__ == "__main__":
    main()
