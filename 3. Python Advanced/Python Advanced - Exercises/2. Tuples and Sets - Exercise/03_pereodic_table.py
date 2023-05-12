chemicals = set()

for _ in range(int(input())):
    elements = input().split()
    [chemicals.add(el) for el in elements]

print(*chemicals, sep="\n")



#2
#
# num = int(input())
# unique_elements = set()

# for i in range(num):
#     elements = input().split()
#     for element in elements:
#         unique_elements.add(element)

# [print(el) for el in unique_elements]
