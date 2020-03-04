import numpy as np


def game_score_v2(number):
    print(f"Number: {number}")
    count = 0
    predict = np.random.randint(1, 100)
    range = 100
    while number != predict:
        print(f"Predict: {predict}")
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count


def score_game(game_score):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=10)
    for number in random_array:
        count_ls.append(game_score(number))
    score = int(np.mean(count_ls))
    print(f"Average score = {score}")
    return score


# number = np.random.randint(1, 100)
# game_score_v2(number)


score_game(game_score_v2)

# count = 0
# number = np.random.randint(1, 100)
#
# while True:
#     predict = int(input("Введите число: "))
#     count += 1
#     if number == predict:
#         break
#     elif number > predict:
#         print(f"Угадываемое число больше {predict}")
#     elif number < predict:
#         print(f"Угадываемое число меньше {predict}")
#
# print(f"Вы угадали число {number} за {count} поппыток.")
