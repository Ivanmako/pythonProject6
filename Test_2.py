word = 'feftef'

word_completion = '_' * len(word)
print(word_completion)

bukva = 'f'
if bukva in word:
    for i in word:
        if i == bukva:
            print(bukva, sep='', end='')
        else:
            print('_', sep='', end='')
