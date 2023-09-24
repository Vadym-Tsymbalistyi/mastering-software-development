# CHAPTER 8
# 1. Составьте список всех структур данных, которые вы использовали при работе
# с Python.
# Списки
# кортежи
# словари
# строки
# масивьі
# THIS IS NOT THE END_)


# CHAPTER 9
# 1. У вас есть массив an_array, состоящий из неотрицательных целых чисел.
# Верните массив, в котором все нечетные элементы массива an_array следуют
# за всеми четными элементами an_array.
def an_array(arr):
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    odd=[]
    for i in arr:
        if i % 2 != 0:
            odd.append(i)
    return odd+even

mas = [1, 2, 4, 24, 43, 4, 5, 6, 8, 8, 65, 765, 345]
result = an_array(mas)
print(result)
