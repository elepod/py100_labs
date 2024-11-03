from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке


for count in counts:
    num_eagle = 0
    num_tails = 0
    # TODO подсчитать количество выпаданий орлов и решек
    for res in range(count + 1):
        if choice(coin) == EAGLE:
            num_eagle += 1
        else:
            num_tails += 1
    result = [num_eagle, num_tails]
    list_freq. append(min(result)/max(result))


    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
