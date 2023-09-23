# Практикум
# 1. Используйте списковое включение, чтобы из следующего списка вернуть
# список всех слов, содержащих более четырех символов: ["selftaught",
# "code", "sit", "eat", "programming", "dinner", "one", "two", "coding",
# "a", "tech"].


def filter_words(list1):
    return [i for i in list1 if len(i) > 4]


list1 = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]

print(filter_words(list1))
