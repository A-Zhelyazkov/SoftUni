import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_name = "numbers.txt"
file_dir = os.path.join(dir_path, file_name)

with open(file_dir, 'r') as nums:
    nums = nums.read().split("\n")
    print(sum(int(i) for i in nums))
