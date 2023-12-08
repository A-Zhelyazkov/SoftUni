def find_variations(arr, idx):
    if idx == len(arr):
        print(*arr, sep=' ')
        return

    for num in range(1, len(arr) + 1):
        arr[idx] = num
        find_variations(arr, idx+1)


n = int(input())

arr = [0] * n

find_variations(arr, 0)