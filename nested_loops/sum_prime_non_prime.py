step = input()
sum_prime = 0
sum_nonprime = 0

while step != "stop":
    n = int(step)
    counter = 0

    if n < 0:
        print("Number is negative.")
        step = input()
        continue

    for number in range(1, n + 1):
        if n % number == 0:
            counter += 1
    if counter == 2:
        sum_prime += n
    else:
        sum_nonprime += n
    step = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")




