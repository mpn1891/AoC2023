import time


def processing(arr):
    print(arr)
    if all(x == 0 for x in arr):
        print(arr[-1])
        yield arr[-1]
        return
    wrk_array = []

    for i in range(len(arr)-1):
        wrk_array.append(int(arr[i+1])-int(arr[i]))
    yield arr[-1]

    yield from processing(wrk_array)


def main():
    # Input processing
    path = ''
    array = []
    ends = []
    answer_arr = []

    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2023\Inputs\D9.txt", "r") as f:
        for line in f.read().splitlines():
            array.append(line.split(' '))
        print(array)

        for i in range(len(array)):
            result = list(processing(array[i]))

            result.reverse()

            for j in range(len(result)-1):
                result[j+1] = int(result[j+1]) + int(result[j])
            print(result)
            answer_arr.append(result[-1])

        answer = 0
        for val in answer_arr:
            answer += val
        print(answer)





if __name__ == "__main__":
    st = time.time()
    main()
    print("----%.2f----" % (time.time() - st))
