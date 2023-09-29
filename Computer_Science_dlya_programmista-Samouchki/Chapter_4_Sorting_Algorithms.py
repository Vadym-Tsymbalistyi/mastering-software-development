# 1. Изучите и напишите алгоритм сортировки, но не пузырьковой, сортировки
# вставками или сортировки слиянием.
# Сортировка вставками
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] >= value:
            a_list[i] = a_list[i - 1]
            i = i - 1
        a_list[i] = value
    return a_list

#Cортировки слиянием
def merge_sort(lst):
   if len(lst) <= 1:
       return lst
   middle = len(lst) // 2
   left = lst[:middle]
   right = lst[middle:]
   left = merge_sort(left)
   right = merge_sort(right)
   return list(merge(left, right))
def merge(left, right):
   res = []
   while len(left) != 0 and len(right) != 0:
       if left[0] < right[0]:
           res.append(left[0])
           left.remove(left[0])
       else:
           res.append(right[0])
           right.remove(right[0])
   if len(left) == 0:
       res += right
   else:
       res += left
   return res
