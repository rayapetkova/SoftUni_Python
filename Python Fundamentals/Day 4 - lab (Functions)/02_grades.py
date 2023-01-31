def grades(score):
    if score < 3.00:
        return "Fail"
    elif score < 3.50:
        return "Poor"
    elif score < 4.50:
        return "Good"
    elif score < 5.50:
        return "Very Good"
    elif score < 6.00:
        return "Excellent"


grade = float(input())
print(grades(grade))