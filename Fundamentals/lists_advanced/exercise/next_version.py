current_version = input().split('.')
current_version = int(''.join(current_version))

next_version = current_version + 1
next_version = str(next_version)
print(f"{next_version[0]}.{next_version[1]}.{next_version[2]}")