def sum_array(nums, i):
    if i >= len(nums) - 1:
        return nums[i]

    return nums[i] + sum_array(nums, i+1)

nums = [int(i) for i in input().split()]

print(sum_array(nums, 0))

