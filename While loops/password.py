user = input()
user_password = input()

password = input()

while password != user_password:
    password = input()

    if password == user_password:
        break

print(f"Welcome {user}!")
