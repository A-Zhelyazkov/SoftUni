import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_name = "text.txt"
file_dir = os.path.join(dir_path, file_name)
if os.path.isfile(file_dir):
    print("File found")
else:
    print("File not found")