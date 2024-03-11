# In the proposed line, delete all repeated words. For example, you are given the string "I am a self-taught programmer
# looking for a job as a programmer.".Your function should return "I am a self-taught programmer looking for
# a job as a.".
from collections import OrderedDict


def remove_dots(del_dots):
    return del_dots.rstrip('.')


def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = OrderedDict()

    for word in words:
        cleaned_word = remove_dots(word)
        unique_words[cleaned_word] = None

    new_sentence = list(unique_words.keys())
    return " ".join(new_sentence)
