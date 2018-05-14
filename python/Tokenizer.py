'''
Tokenizer

Converts output from lex into a list of tokens and their types

List of strings -> List of (value, type)

Beau Miller, Texas Tech. September 2017
'''

from Lexer import *
import re


def tokenize(definition_list):

    list_of_token_lists = []

    next_digit_negative = False
    prev_token = None

    for definition in definition_list:
        token_list = []
        for lex in definition:

            if lex.isdigit():
                if next_digit_negative:
                    token = -int(lex)
                    next_digit_negative = False
                else:
                    token = int(lex)

            elif lex == 'True':
                token = True

            elif lex == 'False':
                token = False

            elif lex == '-':
                if prev_token.isdigit() or prev_token.isalnum():
                    token = '-'
                else:
                    next_digit_negative = True
                    continue

            # Matches repeating decimal expressions
            # and converts it to a float where the
            # repeated decimal is only repeated once

            elif re.match("\d*\.\d*\(\d+\.\.\)", lex):

                non_repeat = lex[:lex.index('(')]
                repeat = lex[lex.index('(')+1:-3]
                print(repeat)
                number = non_repeat + repeat
                print(number)
                token = float(number)

            else:
                token = lex

            token_list.append(token)
            prev_token = lex
        list_of_token_lists.append(token_list)

    return list_of_token_lists


