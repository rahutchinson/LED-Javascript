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

    for lemma in lemma_list:

        if lemma.isdigit():
            token = int(lemma)

        elif lemma == 'True':
            token = True

        elif lemma == 'False':
            token = False

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

    return token_list


# print(lex("True"))
# print(lex("[5,True]"))
# print(tokenize(lex("alpha := lambda x: x + 5")))

# print(tokenize(lex("2+2^(4-4/5)-(18^1/5)")))
