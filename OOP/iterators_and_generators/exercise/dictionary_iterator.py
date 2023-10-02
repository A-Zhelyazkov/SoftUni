class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.items = list(self.dictionary.items())
        self.n = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= len(self.items) - 1:
            raise StopIteration

        self.n += 1
        return self.items[self.n]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
