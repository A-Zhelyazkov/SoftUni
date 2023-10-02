import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "my_first_file.txt"
file_dir = os.path.join(curr_dir, file_name)

if os.path.isfile(file_dir):
    os.remove(file_dir)
else:
    print(f"File already deleted!")