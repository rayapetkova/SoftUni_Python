class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.start = len(obj) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration

        current_number = self.obj[self.start]
        self.start -= 1
        return current_number


# Test code:

# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
