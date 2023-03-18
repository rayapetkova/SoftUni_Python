import re

n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for i in range(n):
    text = input()
    product_group = ""
    if re.match(pattern, text):
        for el in text:
            if el.isdigit():
                product_group += el
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print(f"Invalid barcode")