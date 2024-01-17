#В предлагаемой строке удалите все повторяющиеся слова. Например, вам
#дана строка "I am a self-taught programmer looking for a job as a programmer.".
#Ваша функция должна вернуть "I am a self-taught programmer looking for
#a job as a.".
def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = set()
    new_sentence = []

    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            new_sentence.append(word)
    return " ".join(new_sentence)


original_sentence = "I am a self-taught programmer looking for a job as a programmer ."
result = remove_duplicate_words(original_sentence)
print(result)
