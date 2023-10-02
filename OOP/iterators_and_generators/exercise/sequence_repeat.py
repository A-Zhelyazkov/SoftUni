class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.number - 1:
            raise StopIteration

        self.current += 1

        return self.sequence[self.current % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


