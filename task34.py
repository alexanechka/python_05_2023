# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не
# настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке

# пара-ра-рам рам-пам-папам па-ра-па-да

def get_phrases(poem_text):
    phrase = []
    phrase_word = ''
    for i in range(len(poem_text)):
        if poem_text[i] == ' ':
            phrase.append(phrase_word)
            phrase_word = ''
        else:
            phrase_word += poem_text[i]

    phrase.append(phrase_word)
    return phrase


def count_vowel_letters(phrase):
    vowel_letters_count = 0
    vowel_letters = ["а", "я", "о", "ё", "у", "ю", "э", "е", "ы", "и"]

    for i in range(len(phrase)):
        if phrase[i].lower() in vowel_letters:
            vowel_letters_count += 1
    return vowel_letters_count


def list_comparison(list_numbers):
    first_value = list_numbers[0]
    equal = True

    for i in range(len(list_numbers)):
        if list_numbers[i] != first_value:
            equal = False

    if equal == True:
        return 'Парам пам-пам'
    else:
        return "Пам парам"


poem = input("Введите стихотворение: ")

result = list(map(count_vowel_letters, get_phrases(poem)))
print(list_comparison(result))

