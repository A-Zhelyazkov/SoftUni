import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "my_first_file.txt"
file_dir = os.path.join(curr_dir, file_name)

with open(file_dir, 'w') as file:
    file.write("I just created my first file!'")
