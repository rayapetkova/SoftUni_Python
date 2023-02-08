students = input().split(", ")

# sorting the list "students" by letters
sorted_by_letters = sorted(students)

# sorting the list "sorted by letters" by length and then we reverse it so we can sort them in descending order
# the words are already sorted by letters and they will not shuffle
sorted_students = sorted(sorted_by_letters, key=len, reverse=True)
print(sorted_students)




#2
#
# students = input().split(", ")
#
# sorted_list = sorted(students, key=lambda x: (-len(x), x))
# print(sorted_list)
