# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
import random
from random import randint

ammount_coins = int(input('Введите кол-во монет: ')) 
side_zero = 0
side_one = 0
coins = [0, 1]
for i in range (ammount_coins):
    random.shuffle (coins)
    print(f'Раскладка монет: {coins}')
    if int (coins[0]) == 0:
        side_zero += 1
    if int (coins[0]) == 1:
        side_one =+1
if side_zero > side_one:
    answer = side_one
else:
    answer = side_zero

print(f'минимальное количество монет, которые нужно перевернуть: {answer}')