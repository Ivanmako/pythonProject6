from random import randrange
word_list = ['клопень', 'крендебобель', 'закавырка', 'студень', 'изподвоподверт', 'аквидук']
def get_word(word):  # возвращает случайное слово из списка word_list в верхнем регистре
    random_word = word[randrange(len(word))].upper()
    return random_word.upper()

def display_hangman(tries): # количество попыток угадывания слова и возвращает текущее состояние игры в графическом виде
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries] # #
def change_word(enter_letter):
    pass
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!', display_hangman(tries), word_completion, sep='\n')
    print('Введите предполагаемую букву или слово целиком:')
    while tries > 0:
        enter_letter = input().upper()
        if not enter_letter.isalpha():
            print('Нужно вводить букву или слово, а не всякую фигню')
            continue
        if enter_letter in guessed_words:
            print('Такая буква уже названа. Нужно ввести другую букву')
            continue
        if enter_letter not in word:
            print('Такой буквы в данном слове нет. Введите другую букву')
            guessed_words.append(enter_letter)
            tries -= 1
            continue
        if enter_letter == word:
            print('Поздравлям! Вы отгодали слово целиком')
        else:
            print('Хотите сыграть еще раз?')
            answer = input()
            if answer.isalpha() and answer == 'да'.upper():
                play(word)
            else:
                break





random_word = get_word(word_list)
play(random_word)

