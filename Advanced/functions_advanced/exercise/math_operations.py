from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)
    count = 1
    while numbers:
        if count == 1:
            kwargs["a"] += numbers.popleft()
        elif count == 2:
            kwargs["s"] -= numbers.popleft()
        elif count == 3:
            num = numbers.popleft()
            if num == 0:
                count += 1
                continue
            kwargs["d"] /= num
        elif count == 4:
            kwargs["m"] *= numbers.popleft()
            count = 0
        count += 1

    sorted_kwargs = sorted(kwargs.items(), key=lambda items: (-items[1], items[0]))
    return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted_kwargs])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))
