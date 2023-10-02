class vowels:
    def __init__(self, sequence):
        self.sequence = sequence
        self.all_vowels = ["a", "e", "i", "u", "y", "o"]
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.sequence) - 1:
            raise StopIteration

        self.current += 1

        if self.sequence[self.current].lower() in self.all_vowels:
            return self.sequence[self.current]
        else:
            return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
