class vowels:
    def __init__(self, text):
        self.text = text
        self.start = -1
        self.vowels = [v for v in self.text if v in "AEIOUYaeiouy"]

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.vowels):
            raise StopIteration

        return self.vowels[self.start]


# Test code:

# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
