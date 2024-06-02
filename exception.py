'''Use of try-catch for error handling '''


try:
    age = int(input('Age>'))
    income = 2000
    risk = income/age
    print(risk)
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Age cannot be Zero")
