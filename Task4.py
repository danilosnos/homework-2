import math

def cartesian_to_polar(x, y):
    """Преобразует декартовы координаты в полярные."""
    radius = math.sqrt(x*2 + y*2)
    phi = math.atan2(y, x)  # Используем atan2 для корректного определения угла
    return radius, phi

# Ввод координат
x, y = map(float, input("Введите декартовы координаты в виде x;y: ").split(';'))

# Преобразование и вывод результата
radius, phi = cartesian_to_polar(x, y)
print(f"Полярный радиус: radius={radius:.3f}")
print(f"Полярный угол: phi={phi:.3f}")
