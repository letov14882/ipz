def fibonacci_iterative(n):
    if n <= 0:
        return "Введіть число більше 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Приклад використання
n = int(input("Введіть номер числа Фібоначчі: "))
print(f"Число Фібоначчі номер {n}: {fibonacci_iterative(n)}")
