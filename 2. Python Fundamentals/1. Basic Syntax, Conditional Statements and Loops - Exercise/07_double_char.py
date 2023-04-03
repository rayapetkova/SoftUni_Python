
while True:
    string_given = input()
    new_string = ""
    if string_given == "End":
        break
    if string_given == "SoftUni":
        continue
    for ch in string_given:
        new_ch = ch * 2
        new_string = new_string + new_ch
    print(new_string)