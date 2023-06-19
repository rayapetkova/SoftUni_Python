from collections import deque


class sequence_repeat:
    def __init__(self, text, repeat):
        self.text = deque(list(text))
        self.repeat = repeat
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.repeat:
            raise StopIteration

        symbol = self.text.popleft()
        self.text.append(symbol)
        self.counter += 1

        return symbol


# Test code:

# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')

# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
