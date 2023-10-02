n = int(input())
pieces = {}
for _ in range(n):
    piece, composer, key = input().split("|")

    pieces[piece] = {"composer": composer, "key": key}

while True:
    data = input()

    if data == "Stop":
        break

    data_args = data.split("|")
    command = data_args[0]
    piece = data_args[1]

    if command == "Add":
        composer = data_args[2]
        key = data_args[3]
        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = data_args[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pieces.items():
    print(f"{piece} -> Composer: {values['composer']}, Key: {values['key']}")