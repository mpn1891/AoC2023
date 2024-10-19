import time
from math import lcm

start_list = {}

def main():
    # Input processing
    path = ''
    cur_location = []

    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D8.txt", "r") as f:
        for line in f.read().splitlines():
            if line.find('=') != -1:
                start, rest = line.split('=')
                rest = rest.replace('(', '')
                rest = rest.replace(')', '')
                rest = rest.replace(',', '')
                start_list[start.strip()] = rest.strip()[:3], rest.strip()[4:]
            elif path == '':
                path = line
    cycles = []
    for element in start_list:
        if element[2] == 'A':
            cur_location.append(element)
            cycles.append(0)
    print(cur_location)
    print(path)

    steps = 0
    reached_end = False

    while not reached_end:
        for char in path:
            steps += 1
            for i in range(len(cur_location)):
                if char == 'R':
                    cur_location[i] = start_list.get(cur_location[i])[1]
                else:
                    cur_location[i] = start_list.get(cur_location[i])[0]
                if cycles[i] == 0:
                    if cur_location[i][2] == 'Z':
                        cycles[i] = steps
                        print(cycles)

            if 0 not in cycles:
                reached_end = True

    answer = cycles[0]
    for i in range(len(cycles)-1):
        answer = lcm(answer, cycles[i+1])

    print(answer)


if __name__ == "__main__":
    st = time.time()
    main()
    print("----%.2f----" % (time.time() - st))
