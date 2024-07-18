import math

def sin_taylor(x, n):
    """Генератор для ряда Тейлора синуса."""
    k = 0
    term = x
    while k < n:
        yield term
        k += 1
        term = -term * x * x / ((2 * k) * (2 * k + 1))

def cos_taylor(x, n):
    """Генератор для ряда Тейлора косинуса."""
    k = 0
    term = 1
    while k < n:
        yield term
        k += 1
        term = -term * x * x / ((2 * k - 1) * (2 * k))

def exp_taylor(x, n):
    """Генератор для ряда Тейлора экспоненты."""
    k = 0
    term = 1
    while k < n:
        yield term
        k += 1
        term = term * x / k

def sum_series(series):
    """Суммирует члены ряда."""
    return sum(series)

x = float(input("Введите значение угла в радианах: "))
n = int(input("Введите количество элементов ряда: "))

# Вычисление сумм рядов
sin_sum = sum_series(sin_taylor(x, n))
cos_sum = sum_series(cos_taylor(x, n))
exp_sum = sum_series(exp_taylor(x, n))

# Вывод результатов
print(f"math.sin(x) − sin(x) = {math.sin(x) - sin_sum:.1e}")
print(f"math.cos(x) − cos(x) = {math.cos(x) - cos_sum:.1e}")
print(f"math.exp(x) − exp(x) = {math.exp(x) - exp_sum:.1e}")