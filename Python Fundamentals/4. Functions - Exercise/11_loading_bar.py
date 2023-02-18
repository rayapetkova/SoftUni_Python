def loading_bar(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    needed_percents_count = int(num // 10)
    needed_percents = "%" * needed_percents_count
    needed_dots = "." * (10 - needed_percents_count)
    return f"{num}% [{needed_percents}{needed_dots}]\nStill loading..."


current_num = int(input())
print(loading_bar(current_num))
