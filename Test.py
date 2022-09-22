from random import randrange
word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА',
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК',
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН',
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН',
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР',
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК',
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА',
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']
def get_word(word):  # возвращает случайное слово из списка word_list в верхнем регистре
    random_word = word[randrange(len(word))].upper()
    return random_word

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
    return stages[tries] #

def change_word(word, guessed_letters ):
    for i in range(len(word)):
        if word[i] in guessed_letters:
            print(word[i], end='')
        else:
            print('_', end='')
    print()

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!', display_hangman(tries), word_completion, sep='\n')
    print(f'У вас {tries} попыток угадать букву. Введите предполагаемую букву или слово целиком:')
    while tries > 0:
        enter_word = input().upper()
        display_hangman(tries)
        if len(enter_word) == 1 and enter_word.isalpha():
            if enter_word in guessed_letters:
                print('Такая буква уже называлась.')
                continue
            elif enter_word not in word:
                tries -= 1
                print('Такой буквы нет.', f'Осталось {tries} попыток', display_hangman(tries), sep='\n')
                guessed_letters.append(enter_word)
            elif enter_word in word:
                guessed_letters.append(enter_word)
                change_word(word, guessed_letters)
                print('Вы угадали букву, вводите следующую')
        elif len(enter_word) > 1 and enter_word.isalpha():
            if enter_word in guessed_words:
                print('Такое слово уже вводилось. Введите новок слово')
            if enter_word != word:
                guessed_words.append(enter_word)
                tries -= 1
                print('Слово введено не верно.', f'Осталось {tries} попыток', display_hangman(tries), sep='\n')
            if enter_word == word:
                print('Поздравляю! Вы угадали слово.', 'Хотите сыграть еще раз?', 'да/нет', sep='\n')
                answer = input().upper()
                if answer == 'ДА'and answer.isalpha():
                    random_word = get_word(word_list)
                    play(random_word)
                elif answer == 'НЕТ' and answer.isalpha():
                    print('Пока!')
                else:
                    print('Что за хрень написал? Давай нормальный ответ')
                    continue
        else:
            print('Вы ввели какую-то хрень.', 'Введите букву или слово', sep='\n')
    else:
        print('Ваши попытки закончились', 'Хотите попробовать еще раз?', 'да/нет', sep='\n')
        while True:
            answer = input().upper()
            if answer == 'ДА' and answer.isalpha():
                random_word = get_word(word_list)
                play(random_word)
            elif answer == 'НЕТ' and answer.isalpha():
                print('Пока!')
            else:
                print('Что за хрень написал? Давай нормальный ответ')
                continue

random_word = get_word(word_list)
play(random_word)

