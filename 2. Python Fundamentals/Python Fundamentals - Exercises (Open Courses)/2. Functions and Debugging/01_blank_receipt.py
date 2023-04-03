def header():
    return f"CASH RECEIPT\n------------------------------"


def body():
    return f"Charged to____________________\nReceived by___________________"


def footer():
    return f"------------------------------\n© SoftUni"


def final():
    print(f"{header()}\n{body()}\n{footer()}")


final()