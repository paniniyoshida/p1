# -*- coding: cp1251 -*-
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        result = "Ошибка: деление на ноль невозможно"
    return result

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Ошибка: невозможно вычислить факториал отрицательного числа"
    else:
        return math.factorial(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def validate_input(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

def get_number_input():
    while True:
        input = raw_input("Введите число: ")
        if validate_input(input):
            return float(input)
        else:
            print("Ошибка: введено некорректное число")

def get_operation_input(operations):
    while True:
        input = raw_input("Выберите операцию ({}): ".format(", ".join(operations)))
        if input in operations:
            return input
        else:
            print("Ошибка: некорректная операция")

def perform_operation(operation, numbers):
    if operation == "add":
        return add(numbers[0], numbers[1])
    elif operation == "subtract":
        return subtract(numbers[0], numbers[1])
    elif operation == "multiply":
        return multiply(numbers[0], numbers[1])
    elif operation == "divide":
        return divide(numbers[0], numbers[1])
    elif operation == "exponentiate":
        return exponentiate(numbers[0], numbers[1])
    elif operation == "square_root":
        return square_root(numbers[0])
    elif operation == "factorial":
        return factorial(int(numbers[0]))
    elif operation == "sine":
        return sine(numbers[0])
    elif operation == "cosine":
        return cosine(numbers[0])
    elif operation == "tangent":
        return tangent(numbers[0])

def main():
    operations = ["add", "subtract", "multiply", "divide", "exponentiate", "square_root", "factorial", "sine", "cosine", "tangent"]
    operation = get_operation_input(operations)

    if operation in ["add", "subtract", "multiply", "divide", "exponentiate"]:
        number1 = get_number_input()
        number2 = get_number_input()
        result = perform_operation(operation, [number1, number2])
        print("Результат: {}".format(result))
    elif operation in ["square_root", "factorial", "sine", "cosine", "tangent"]:
        number = get_number_input()
        result = perform_operation(operation, [number])
        print("Результат: {}".format(result))

if __name__ == "__main__":
    main()

