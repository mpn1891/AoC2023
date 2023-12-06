import math


def main():
    array = []
    ans = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D6.txt", "r") as f:
        for line in f.read().split('\n'):
            array.append(line)

    time_arr = array[0].split()
    time_arr.pop(0)
    dist_arr = array[1].split()
    dist_arr.pop(0)

    for time, dist in zip(time_arr, dist_arr):
        low, high = quadratic(-1, int(time), -int(dist))

        if int(dist) >= int(time)*low-low**2:
            low = low + 1
        if int(dist) >= int(time)*high-high**2:
            high = high - 1

        print(high-low+1)
        ans.append(high-low+1)
    mul = 1
    for x in ans:
        mul *= x
    print(mul)


def quadratic(a, b, c):
    four_ac = 4 * a * c
    sqrt_val = math.sqrt(b**2-four_ac)
    ans1 = (-b + sqrt_val)/(2*a)
    ans2 = (-b - sqrt_val) / (2 * a)
    return round(ans1), round(ans2)


if __name__ == "__main__":
    main()
