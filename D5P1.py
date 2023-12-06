from collections import defaultdict


def main():
    array = []
    seeds = []
    blanks = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D5.txt", "r") as f:
        for val in f.read().split('\n'):
            array.append(val)

    # Parse every line
    for i, line in enumerate(array):
        if i == 0:
            a, b = line.split(':')
            seeds = b.split()
        elif line == '':
            blanks.append(i)

    blanks.append(len(array))

    print(blanks)
    # blanks should represent start and stops of maps relatively anyway
    for j in range(blanks[0]+2, blanks[1]):
        seed_to_soil.append(array[j].split())
    for j in range(blanks[1]+2, blanks[2]):
        soil_to_fertilizer.append(array[j].split())
    for j in range(blanks[2] + 2, blanks[3]):
        fertilizer_to_water.append(array[j].split())
    for j in range(blanks[3] + 2, blanks[4]):
        water_to_light.append(array[j].split())
    for j in range(blanks[4] + 2, blanks[5]):
        light_to_temperature.append(array[j].split())
    for j in range(blanks[5] + 2, blanks[6]):
        temperature_to_humidity.append(array[j].split())
    for j in range(blanks[6] + 2, blanks[7]):
        humidity_to_location.append(array[j].split())

    temp_seeds = translate(seeds, seed_to_soil)
    temp_seeds = translate(temp_seeds, soil_to_fertilizer)
    temp_seeds = translate(temp_seeds, fertilizer_to_water)
    temp_seeds = translate(temp_seeds, water_to_light)
    temp_seeds = translate(temp_seeds, light_to_temperature)
    temp_seeds = translate(temp_seeds, temperature_to_humidity)
    temp_seeds = translate(temp_seeds, humidity_to_location)



    print(temp_seeds)

    print(min(temp_seeds))


def translate(seeds, loc_map) -> list:

    ret = []
    valid_source = []
    translated_seeds = []
    for line in loc_map:
        total_source = int(line[1]) + int(line[2]) - 1
        total_dest = int(line[0]) + int(line[2]) - 1
        valid_source.append([int(line[1]), total_source])
        translated_seeds.append([int(line[0]), total_dest])
    for seed in seeds:
        break_flag = False
        # print('seed', seed)
        for i, source in enumerate(valid_source):
            # print('source', source)
            if int(source[0]) <= int(seed) <= int(source[1]):
                # print('found')
                # print(loc_map[i])
                ret.append(int(loc_map[i][0]) - int(source[0]) + int(seed))
                break_flag = True
                break
        if break_flag:
            continue
        else:
            ret.append(seed)
    return ret


if __name__ == "__main__":
    main()
