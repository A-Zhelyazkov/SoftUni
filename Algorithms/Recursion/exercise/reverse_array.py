def reverse_arr(arr, start=0, end=0):
    if end == 0:
        end = len(arr) - 1
    if end <= start:
        return ' '.join(str(i) for i in arr)
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_arr(arr, start+1, end-1)


arr = [int(i) for i in input().split()]

print(reverse_arr(arr))

