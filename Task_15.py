n, *cards = map(int, input().split())
sum_all = (n * (n + 1)) // 2  # вычисляем сумму всех номеров от 1 до N
sum_left = sum(cards)  # вычисляем сумму номеров оставшихся карточек
print(sum_all - sum_left)  # выводим номер потерянной карточки
