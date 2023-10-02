path = input().split("\\")
name, file_ext = path[-1].split(".")

print(f"File name: {name}")
print(f"File extension: {file_ext}")