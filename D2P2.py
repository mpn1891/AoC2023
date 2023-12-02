import re


def main():
    array = []
    word_array = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D2.txt", "r") as f:
        for val in f.read().splitlines():
            array.append(val)

    for s in array:
        # splits
        words = re.split('Game |: |, |' ' ', s)
        # removes any empty elements
        words = [item for item in words if item != '']
        word_array.append(words)

    reset_game = False
    end_game = False
    power = []

    for game in word_array:
        temp_blue = 0
        temp_red = 0
        temp_green = 0
        min_blue = 0
        min_red = 0
        min_green = 0

        for pull in range(1, len(game) - 1, 2):
            color = game[pull+1]
            if ';' in color:
                reset_game = True
                color = color.replace(';', '')
            if pull == len(game) - 2:
                end_game = True

            amount = int(game[pull])

            if color == 'blue':
                temp_blue += amount
            elif color == 'green':
                temp_green += amount
            elif color == 'red':
                temp_red += amount

            if reset_game:
                reset_game = False
                if temp_blue > min_blue:
                    min_blue = temp_blue
                if temp_red > min_red:
                    min_red = temp_red
                if temp_green > min_green:
                    min_green = temp_green
                temp_blue = 0
                temp_red = 0
                temp_green = 0

            if end_game:
                end_game = False
                if temp_blue > min_blue:
                    min_blue = temp_blue
                if temp_red > min_red:
                    min_red = temp_red
                if temp_green > min_green:
                    min_green = temp_green
                power.append((min_blue*min_red*min_green))

    answer = 0
    for x in power:
        answer += int(x)

    print(answer)


if __name__ == "__main__":
    main()
