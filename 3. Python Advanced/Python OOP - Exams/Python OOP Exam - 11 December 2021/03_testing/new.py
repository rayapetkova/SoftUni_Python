final = {'a': 24, 'b': 19, 'd': 28, 'c': 28,  'e': 17, 'f': 18}
sorted_lst = list(sorted(final.items(), key=lambda x: (-x[1], x[0])))

print(sorted_lst)