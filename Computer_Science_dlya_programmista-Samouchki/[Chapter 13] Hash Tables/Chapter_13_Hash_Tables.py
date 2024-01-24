# В предлагаемой строке удалите все повторяющиеся слова. Например, вам
# дана строка "I am a self-taught programmer looking for a job as a programmer.".
# Ваша функция должна вернуть "I am a self-taught programmer looking for
# a job as a.".
from collections import OrderedDict
#import string


def remove_dots(del_dots):
    return del_dots.rstrip('.')


def remove_duplicate_words(sentence):
    #translator = str.maketrans('', '', string.punctuation)
    words = sentence.split()
    unique_words = OrderedDict()

    for word in words:
        #cleaned_word = word.translate(translator)
        cleaned_word = remove_dots(word)
        unique_words[cleaned_word] = None

    new_sentence = list(unique_words.keys())
    return " ".join(new_sentence)


sentence = "I am a self-taught programmer looking for a job as a programmer."
result = remove_duplicate_words(sentence)
print(result)
