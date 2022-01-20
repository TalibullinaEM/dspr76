import numpy as np

def random_predict(number: int = 1) -> int:# первый вариант - случайный выбор числа в заданном диапазоне
    """Рандомно загадываем число и угадываем его, сравниваем со случайным из первонач.интервала.
    Затем, в зависимости от результата, границы интервала изменяются. 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max = 101
    min = 1

    while True:
        count += 1
        predict_number = np.random.randint(min, max) # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min = predict_number
        else :
            max = (predict_number + 1)
    return count



def random_predict_2(number: int = 1) -> int:#второй вариант - в диапазоне всегда выбирается его "середина"
    """Рандомно загадываем число и угадываем его следующим образом. Сравниваем с новым числом, равного половине
    первоначального интервала. Каждый раз границы интервала меняются в зависимости от результата

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max = 101
    min = 1

    while True:
        count += 1
        predict_number = int((min + max)/2) #  cередина интервала
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            min = predict_number
        else :
            max = predict_number 
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток угадывается число, при 1000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #  Закрепили сид
    random_array = np.random.randint(1, 101, size = (1000)) #   создали массив из 1000 целых чисел от 1 до 100 по кот.проверяется алгоритм 
    for number in random_array :
        count_ls.append(random_predict(number)) # в список добавляется количество попыток по каждому числу
    score = int(np.mean(count_ls))     #  посчитали среднее этого списка
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict_2)
score_game(random_predict)
    