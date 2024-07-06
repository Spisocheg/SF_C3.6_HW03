from django import template

register = template.Library()

bad_words_list = ['semper', 'pulvinar', 'pulvinar', 'amet', 'justo', 'lorem', 'condimentum', 'dictum', 'lectus']
punc_marks = ['.', ',', ';', ':', '!', '?']


@register.filter()
def censor(value):
    for bad_word in bad_words_list:
        value = value.replace(bad_word[1:], '*' * len(bad_word[1:]))

    return value
