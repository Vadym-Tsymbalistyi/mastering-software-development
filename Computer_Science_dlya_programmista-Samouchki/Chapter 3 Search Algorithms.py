# 1. Дан список слов в алфавитном порядке. Напишите функцию, которая вы-
# полнит двоичный поиск слова и вернет ответ о том, имеется ли оно в списке.


def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1

    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


a_list = ['apple', 'banana','kiwi', 'orange', 'plum']
n = 'apple'
result = binary_search(a_list, n)
if result:
    print(f'{n} found in the list' )
else:
    print(f'{n}found in the list')
