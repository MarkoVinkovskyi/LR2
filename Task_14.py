from typing import List

def read_sequence() -> List[int]:
    """Считывает последовательность целых чисел из входного потока"""
    sequence = []
    while True:
        n = int(input())
        if n == 0:
            if len(sequence) == 0:
                # Если последовательность пуста, то просим пользователя ввести еще раз
                print("Последовательность не должна быть пустой. Введите еще раз:")
                continue
            else:
                break
        sequence.append(n)
    return sequence

def sum_sequence(sequence: List[int]) -> int:
    """Вычисляет сумму элементов последовательности"""
    return sum(sequence)

# Декоратор для измерения времени выполнения функции
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

# Используем декоратор для измерения времени выполнения функции
@timer
def main():
    sequence = read_sequence()
    s = sum_sequence(sequence)
    print(s)

if __name__ == '__main__':
    main()

