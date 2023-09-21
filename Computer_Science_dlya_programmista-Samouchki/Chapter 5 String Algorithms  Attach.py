# Практикум
# 1. Используйте списковое включение, чтобы из следующего списка вернуть
# список всех слов, содержащих более четырех символов: ["selftaught",
# "code", "sit", "eat", "programming", "dinner", "one", "two", "coding",
# "a", "tech"].


list1 = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
list = [i for i in list1 if len(i) > 4]
print(list)
