class reverse_iter:
    def __init__(self, sequence):
        self.iterable = sequence
        self.start = len(self.iterable)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            raise StopIteration

        self.start -= 1
        return self.iterable[self.start]


reversed_list = reverse_iter("asd")
for item in reversed_list:
    print(item)
