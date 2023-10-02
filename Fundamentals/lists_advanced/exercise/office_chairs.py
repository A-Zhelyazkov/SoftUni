rooms = int(input())
free_chairs = 0
game_on = True
for i in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])

    if len(chairs) >= visitors:
        free_chairs += len(chairs) - visitors
    else:
        needed_chairs = visitors - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {i}")
        game_on = False

if game_on:
    print(f"Game On, {free_chairs} free chairs left")
