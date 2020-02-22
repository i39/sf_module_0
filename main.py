import numpy as np
MAX = 100

def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, MAX+1)  # предполагаемое число
        if number == predict:
            break
    return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1, MAX)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    '''Поскольку мы  имеем строго ограниченный набор чисел от 1 до 100
    то попробуем использовать простой  бинарный поиск
    как  ни страанно от работает медленее чем разбег от случайного числа
    game-core_v2'''

    mid = MAX // 2
    low = 0
    high = MAX

    while mid != number and low <= high:
        if number > mid:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return mid


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, MAX+1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем все версии и сравниваем
score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
