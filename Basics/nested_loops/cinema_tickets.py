operation = input()
student_counter = 0
kid_counter = 0
standard_counter = 0
total_tickets = 0
while operation != "Finish":
    free_spots = int(input())
    counter = 0
    movie = operation
    while True:
        ticket_type = input()
        if ticket_type == "End":
            percent_full = (counter / free_spots) * 100
            print(f"{movie} - {percent_full:.2f}% full.")
            break
        total_tickets += 1
        if ticket_type == "standard":
            standard_counter += 1
        if ticket_type == "kid":
            kid_counter += 1
        if ticket_type == "student":
            student_counter += 1
        counter += 1
        if counter == free_spots:
            print(f"{movie} - 100.00% full.")
            break
    operation = input()

print(f"Total tickets: {total_tickets}")
print(f"{(student_counter/total_tickets)*100:.2f}% student tickets.")
print(f"{(standard_counter/total_tickets)*100:.2f}% standard tickets.")
print(f"{(kid_counter/total_tickets)*100:.2f}% kids tickets.")