def stock_availability(*args):
    boxes, second, others = args[0], args[1], args[2:]
    if second == "delivery":
        boxes.extend(others)
        return boxes

    elif second == "sell":
        if len(others) == 0:
            boxes.pop(0)
            return boxes

        if str(others[0]).isdigit():
            del boxes[:others[0]]
            return boxes

        for product in others:
            if product in boxes:
                boxes = [el for el in boxes if el != product]

        return boxes


# Test inputs:

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
