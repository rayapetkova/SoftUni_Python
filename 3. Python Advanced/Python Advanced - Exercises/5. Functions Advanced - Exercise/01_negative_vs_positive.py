def negatives_and_positives(*args):
    result_string = ""
    negatives_sum = sum([num for num in args if num < 0])
    positives_sum = sum([num for num in args if num > 0])

    if abs(negatives_sum) > positives_sum:
        result_string = "The negatives are stronger than the positives"

    else:
        result_string = "The positives are stronger than the negatives"

    return f"{negatives_sum}\n{positives_sum}\n{result_string}"


numbers = [int(n) for n in input().split()]
print(negatives_and_positives(*numbers))
