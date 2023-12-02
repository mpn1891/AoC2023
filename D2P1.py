import re


def main():
    array = []
    word_array = []
    max_red = 12
    max_green = 13
    max_blue = 14
    possible_games = []

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

    for game in word_array:
        temp_blue = 0
        temp_red = 0
        temp_green = 0
        for pull in range(1, len(game) - 1, 2):

            color = game[pull + 1]
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
                if temp_blue > max_blue or temp_red > max_red or temp_green > max_green:
                    break
                else:
                    temp_blue = 0
                    temp_red = 0
                    temp_green = 0

            if end_game:
                end_game = False
                if temp_blue <= max_blue and temp_red <= max_red and temp_green <= max_green:
                    possible_games.append(game[0])

    answer = 0
    for x in possible_games:
        answer += int(x)

    print(answer)


if __name__ == "__main__":
    main()
