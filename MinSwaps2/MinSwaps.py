import os


def minimumSwaps(arr):
    sorted_arr = sorted(arr)
    count = 0
    values_index_dict = {v: i for i, v in enumerate(arr)}
    for i, v in enumerate(arr):
        correct_value = sorted_arr[i]
        if v != correct_value:
            swap_index = values_index_dict[correct_value]
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
            values_index_dict[v] = swap_index
            values_index_dict[correct_value] = i
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
