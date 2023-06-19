class countdown_iterator:
    def __init__(self, num):
        self.num = num
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.end:
            raise StopIteration

        curr_num = self.num
        self.num -= 1
        return curr_num


# Test code:

# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
