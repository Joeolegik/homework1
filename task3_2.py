list_eng_rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    if eng_word[0] == eng_word[0].upper():
        eng_word = eng_word.lower()
        return list_eng_rus[eng_word].capitalize()
    else:
        return list_eng_rus[eng_word]

print(num_translate_adv('One'))
print(num_translate_adv('two'))
print(num_translate_adv('Three'))
print(num_translate_adv('four'))
print(num_translate_adv('Five'))
print(num_translate_adv('Six'))
print(num_translate_adv('Seven'))
print(num_translate_adv('Eight'))
print(num_translate_adv('Nine'))
print(num_translate_adv('Ten'))
