from random import randrange

word_list = ['клопень', 'крендебобель', 'закавырка', 'студень', 'изподвоподверт', 'аквидук']

def get_word():  # возвращает случайное слово из списка word_list в верхнем регистре
    return word_list[randrange(len(word_list))].upper()


print(get_word())