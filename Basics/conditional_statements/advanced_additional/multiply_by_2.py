while True:
    a = float(input())
    if a < 0:
        print("Negative number!")
        break

    total = a * 2
    print(f"Result: {total:.2f}")