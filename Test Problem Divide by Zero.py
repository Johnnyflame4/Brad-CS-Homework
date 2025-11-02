def divide_by_non_zero(a, b):
    try:
        answer = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

divide_by_non_zero(10, 0)