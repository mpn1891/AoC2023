import time


class node:
    start = ''
    left = ''
    right = ''


start_list = {}


def main():
    # Input processing
    path = ''
    cur_location = 'AAA'

    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D8.txt", "r") as f:
        for line in f.read().splitlines():
            if line.find('=') != -1:
                print(line)
                start, rest = line.split('=')
                rest = rest.replace('(', '')
                rest = rest.replace(')', '')
                rest = rest.replace(',', '')
                start_list[start.strip()] = rest.strip()[:3], rest.strip()[4:]
            elif path == '':
                path = line
    print(path)
    print(start_list)
    print(start_list.get(cur_location))
    steps = 0
    while cur_location != 'ZZZ':
        for char in path:
            steps += 1
            if char == 'R':
                cur_location = start_list.get(cur_location)[1]
            else:
                cur_location = start_list.get(cur_location)[0]

    print(steps)




if __name__ == "__main__":
    st = time.time()
    main()
    print("----%.2f----" % (time.time() - st))
