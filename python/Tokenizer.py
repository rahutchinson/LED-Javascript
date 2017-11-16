'''
Tokenizer

Converts output from lemmatize into a list of tokens and their types

List of strings -> List of (value, type)

Beau Miller, Texas Tech. September 2017
'''

from Lexer import lex
import re


def tokenize(lemma_list):

    token_list = []

    next_digit_negative = False
    prev_token = None

    for lemma in lemma_list:

        if lemma.isdigit():
            if next_digit_negative:
                token = -int(lemma)
                next_digit_negative = True
            else:
                token = int(lemma)

        elif lemma == 'True':
            token = True

        elif lemma == 'False':
            token = False

        elif lemma == '-':
            if prev_token.isdigit():
                token = '-'
            else:
                next_digit_negative = 1
                continue

        # Matches repeating decimal expressions
        # and converts it to a float where the 
        # repeated decimal is only repeated once

        elif re.match("\d*\.\d*\(\d+\.\.\)", lemma):

            non_repeat = lemma[:lemma.index('(')]
            repeat = lemma[lemma.index('(')+1:-3]
            print(repeat)
            number = non_repeat + repeat
            print(number)
            token = float(number)

        else:
            token = lemma

        token_list.append(token)
        prev_token = lemma

    return token_list


# print(lex("True"))
# print(lex("[5,True]"))
# print(tokenize(lex("alpha := lambda x: x + 5")))

#print(tokenize(lex("f(x,y,z) := t1 if p1")))
print(tokenize(lex("4-1-5-6-14+(-45) ^ 29 ^ -79 +5")))
