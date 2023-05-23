first, second, third = ["{", "}"], ["(", ")"], ["[", "]"]

stack_line = []
expression = input()
found = False

for element in expression:
    if element in "{([":
        stack_line.append(element)
    else:
        if stack_line:
            popped_element = stack_line.pop()
            if element == first[1] and popped_element == first[0]:
                found = False

            elif element == second[1] and popped_element == second[0]:
                found = False

            elif element == third[1] and popped_element == third[0]:
                found = False

            else:
                stack_line.append(popped_element)
                found = True
                break
        else:
            found = True
            break

if stack_line or found:
    print("NO")

else:
    print(f"YES")

    
    
    
    
   
   


#2
#
# dictionary = {
#     "{": "}",
#     "(": ")",
#     "[": "]"
# }


# stack_line = []
# expression = input()
# found = False

# for element in expression:
#     if element in "{([":
#         stack_line.append(element)
#     else:
#         if stack_line:
#             popped_element = stack_line.pop()
#             if not dictionary[popped_element] == element:
#                 found = True
#                 break
#         else:
#             found = True
#             break

# if stack_line or found:
#     print("NO")
# else:
#     print(f"YES")
