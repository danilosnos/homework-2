def get_fib_numbers(qty=None):
    a, b = 0, 1
    count = 0
    while qty is None or count < qty:
        yield a
        a, b = b, a + b
        count += 1
        if count >= 100:  # Искусственное ограничение на 100 элементов
            break

fib_numbers = list(get_fib_numbers(10))
assert len(fib_numbers) == 10
print(fib_numbers)