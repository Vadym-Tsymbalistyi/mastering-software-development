# Use list inclusion to return from the following list a list of all words with more than four characters:
# ["selftaught","code", "sit", "eat", "programming", "dinner", "one", "two", "coding","a", "tech"].


def filter_words(list1):
    return [i for i in list1 if len(i) > 4]
