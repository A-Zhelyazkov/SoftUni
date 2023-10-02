def get_primes(num_list):
    for num in num_list:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num



print(list(get_primes([-2, 0, 0, 1, 1, 0])))