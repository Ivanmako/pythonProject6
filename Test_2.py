from random import randrange

word_list = ['клопень', 'крендебобель', 'закавырка', 'студень', 'изподвоподверт', 'аквидук']

def get_word(word):  # возвращает случайное слово из списка word_list в верхнем регистре
    return word[randrange(len(word))].upper()


print(get_word(word_list))