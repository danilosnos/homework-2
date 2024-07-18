import operator
import re
import logging

# Настройка логгера
logging.basicConfig(filename='logs.log', level=logging.ERROR, format='%(asctime)s | %(levelname)s | %(message)s')

# Операции калькулятора
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


# Функции для операций
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def truediv(a, b):
    return a / b


def calculate_expression(expression):
    try:
        expression = re.sub(r'\s', '', expression)  # Удаляем пробелы из выражения
        for op in ['+', '-', '*', '/']:
            if op in expression:
                operator = op
                operands = expression.split(operator)
                operand1 = float(operands[0])
                operand2 = float(operands[1])
                break

        result = operations[operator](operand1, operand2)
        return result

    except Exception as e:
        logging.error(f'could not calculate expression {expression}: {e}')


# Чтение и обработка выражений из файла
with open('exprs.txt', 'r') as file:
    lines = file.readlines()

results = []
for i, line in enumerate(lines, start=1):
    line = line.strip()
    if line:
        result = calculate_expression(line)
        if result is not None:
            results.append((i, result))

# Запись результатов вычислений в файл
with open('results.txt', 'w') as file:
    for result in results:
        file.write(f'{result[0]} {result[1]}\n')