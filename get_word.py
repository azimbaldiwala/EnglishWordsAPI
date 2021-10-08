import random
import json


def get_word(word_size=0, word_initial='-'):
    """

    :param word_size: Size of word that is to be returned
    :param word_initial: Initial of the word that is to be returned
    :return: the word and its meaning
    """

    file = open('dictionary.json', )
    data = json.load(file)
    word = list(data.keys())
    meaning = list(data.values())
    rand_word = random.randint(0, 102217)
    index = 0

    if word_size != 0 and word_initial != '-':
        if word_size != 0:
            if word_size > 35:
                return "Error[Maximum Size of word can be 35]"

            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't',
                       'u', 'v', 'w', 'x', 'y', 'z']
            if word_initial.lower() not in letters:
                return "Error[Character must be an alphabet]"

            i = random.randint(0, 102217)

            while True:

                if i >= 102217:
                    i = random.randint(0, 102217)

                if len(word[i]) == word_size and word[i][0] == word_initial:
                    return word[i], meaning[i].split(';')

                i += 1

    if word_size != 0:
        if word_size > 35:
            return "Error[Maximum Size of word can be 35]"
        i = random.randint(0, 102217)
        while True:

            if i >= 102217:
                i = random.randint(0, 102217)

            if len(word[i]) == word_size:
                return word[i], meaning[i].split(';')

            i += 1

    if word_initial != '-':
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
        if word_initial.lower() not in letters:
            return "Error[Character must be an alphabet]"

        i = random.randint(0, 102217)
        while True:

            if i >= 102217:
                i = random.randint(0, 102217)

            if word[i][0] == word_initial:
                return word[i], meaning[i].split(';')

            i += 1

    return word[rand_word], meaning[rand_word].split(';')


