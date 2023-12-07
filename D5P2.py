from collections import defaultdict


def main():
    array = []
    seed_ranges = []
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
            temp = b.split()
            for x in range(0, len(temp), 2):
                z = int(temp[x]) + int(temp[x + 1])
                seed_ranges.append([temp[x], z])
        elif line == '':
            blanks.append(int(i))

    blanks.append(int(len(array)))
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

    seed_ranges = [[int(element) for element in row] for row in seed_ranges]
    print(seed_ranges)
    seed_to_soil = [[int(element) for element in row] for row in seed_to_soil]
    soil_to_fertilizer = [[int(element) for element in row] for row in soil_to_fertilizer]
    fertilizer_to_water = [[int(element) for element in row] for row in fertilizer_to_water]
    water_to_light = [[int(element) for element in row] for row in water_to_light]
    light_to_temperature = [[int(element) for element in row] for row in light_to_temperature]
    temperature_to_humidity = [[int(element) for element in row] for row in temperature_to_humidity]
    humidity_to_location = [[int(element) for element in row] for row in humidity_to_location]

    temp_ranges = translate(seed_ranges, seed_to_soil)
    temp_ranges = translate(temp_ranges, soil_to_fertilizer)
    temp_ranges = translate(temp_ranges, fertilizer_to_water)
    temp_ranges = translate(temp_ranges, water_to_light)
    temp_ranges = translate(temp_ranges, light_to_temperature)
    temp_ranges = translate(temp_ranges, temperature_to_humidity)
    temp_ranges = translate(temp_ranges, humidity_to_location)

    print(min(temp_ranges)[0])



def translate(ranges, loc_map) -> list:
    affected = []
    map_info = []

    for dest, src, rng in loc_map:
        map_info.append([int(src), int(src) + int(rng), dest])

    for src_st, src_ed, destination in map_info:
        not_affected = []

        while ranges:
            seed_st, seed_ed = ranges.pop()
            print(seed_st, seed_ed)

            before = [seed_st, min(seed_ed, src_st)]
            inter = [max(seed_st, src_st), min(src_ed, seed_ed)]
            after = [max(seed_st, src_ed), seed_ed]
            print(before,inter,after)

            if before[1] > before[0]:
                not_affected.append(before)
            if inter[1] > inter[0]:
                affected.append([inter[0]-src_st+destination, inter[1]-src_st+destination])
            if after[1] > after[0]:
                not_affected.append(after)
        ranges = not_affected

    return affected + not_affected


if __name__ == "__main__":
    main()
