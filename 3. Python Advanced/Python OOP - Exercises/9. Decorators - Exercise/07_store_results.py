class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as final:
            final.write(f"Function '{self.func.__name__}' was called. Result: {self.func(*args, *kwargs)}\n")


# Test code:

# @store_results
# def add(a, b):
#     return a + b
#
#
# @store_results
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)
