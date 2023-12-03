import re


def main():
    array = []
    mul_array = []
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D3.txt", "r") as f:
        for val in f.read().splitlines():
            array.append(val)

    num_lines = len(array) - 1
    line_length = len(array[0]) - 1

    # iterate through all lines/characters
    for i in range(0, len(array)):
        j = 0
        while j < len(array[i]) - 1:
            # check if it's a digit
            if array[i][j] == '*':
                temp_start = j
                mul_array.append(check_surroundings(array, i, temp_start, num_lines, line_length))
            j += 1

    p2 = 0
    for y in mul_array:
        p2 += y

    print(p2)


def check_surroundings(data, line, start_character, total_line, total_len) -> int:
    print(line, start_character, total_line, total_len)
    # gets bounds
    temp_array = []
    start_pos = []

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
    if start_character == total_len:
        max_character = start_character
    else:
        max_character = start_character + 1

    for i in range(min_line, max_line + 1):
        for j in range(min_character, max_character + 1):
            if data[i][j].isdigit():
                temp_array.append([i, j])

    for pair in temp_array:
        print(pair)
        if pair[1] == 0:
            start_pos.append([pair[0], pair[1]])
        else:
            start_pos.append(get_start_of_number(pair[0], pair[1], data))
    print('list', start_pos)

    unique_starts = remove_duplicates(start_pos)
    print(unique_starts)

    if len(unique_starts) == 2:
        ret_value = int(unique_starts[0][2]) * int(unique_starts[1][2])
        return ret_value
    else:
        return 0
    # add all parts of the engine array


# this function can be cleaned up
def get_start_of_number(line, character, data) -> list:
    for i in range(character, -1, -1):
        print(data[line][i])
        if i == 0:
            if data[line][i].isdigit():
                return [line, i, data[line][i:get_end_of_number(line, character, data)]]
            else:
                return [line, i + 1, data[line][i + 1:get_end_of_number(line, character, data)]]
        elif data[line][i].isdigit():
            continue
        else:
            return [line, i + 1, data[line][i + 1:get_end_of_number(line, character, data)]]


def get_end_of_number(line, character, data) -> int:
    for i in range(character, len(data[0])):
        if data[line][i].isdigit():
            continue
        return i


def remove_duplicates(local_list) -> list:
    # Use a set to store unique elements
    unique_set = set()

    # Use a list to store the result
    result_list = []

    for sublist in local_list:
        # Convert each sublist to a tuple to make it hashable and check for uniqueness
        tuple_sublist = tuple(sublist)

        # If the tuple is not in the set, add it to both the set and the result list
        # was testing sets, but just went with  lists
        if tuple_sublist not in unique_set:
            unique_set.add(tuple_sublist)
            result_list.append(sublist)

    return result_list


if __name__ == "__main__":
    main()
