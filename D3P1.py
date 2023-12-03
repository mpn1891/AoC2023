import re


def main():
    array = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D3.txt", "r") as f:
        for val in f.read().splitlines():
            array.append(val)

    for x in array:
        print(x)
    num_lines = len(array) - 1
    line_length = len(array[0]) - 1
    sum_array = []

    # iterate through all lines/characters
    print(len(array))
    print(len(array[0]))
    for i in range(0, len(array)):
        print(i)
        j = 0
        while j < len(array[i]) - 1:
            print(j)
            # check if it's a digit
            if array[i][j].isdigit():
                temp_start = j
                while array[i][j].isdigit():
                    temp_end = j
                    if j == len(array[i]) - 1:
                        break
                    j += 1
                print(j)

                symbol_check = check_surroundings(array, i, temp_start, temp_end, num_lines, line_length)
                if symbol_check:
                    sum_array.append(array[i][temp_start:temp_end+1])
                    continue
            else:
                j += 1

    # Now that we have the list
    print(sum_array)
    p1 = 0
    for x in sum_array:
        p1 += int(x)
    print(p1)

    # if we find one, add this number to the engine array


def check_surroundings(data, line, start_character, end_character, total_line, total_len) -> bool:
    print(line, start_character, end_character, total_line, total_len)
    # gets bounds
    if line == 0:
        min_line = 0
    else:
        min_line = line - 1
    if line == total_line:
        max_line = line
    else:
        max_line = line + 1

    if start_character == 0:
        min_character = 0
    else:
        min_character = start_character - 1
    if end_character == total_len:
        max_character = end_character
    else:
        max_character = end_character + 1

    for i in range(min_line, max_line + 1):
        for j in range(min_character, max_character + 1):
            print('checking', i, j)
            if data[i][j].isdigit() or data[i][j] == '.':
                continue
            else:
                print('found', data[i][j])
                return True

    return False
    # add all parts of the engine array


if __name__ == "__main__":
    main()
