def read_next(*args):
    for seq in args:
        for curr_char in seq:
            yield curr_char

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
