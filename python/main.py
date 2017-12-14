from python.Lexer import *
from python.Tokenizer import *
from python.LED_GameParser import *
from python.LED_GameCompiler_js import *



FILENAME = "TicTacToe"


def main():
    LED_file = open_LED_file(FILENAME)
    LED_code = preprocess_codeblocks(LED_file)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    pared_LED = parse(tokenized_LED)
    compiled_LED_to_js = comp_func(pared_LED)
    return compiled_LED_to_js

def compile_LED_to_JS(LED_code_string):
    LED_code = preprocess_codeblocks(LED_code_string)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    pared_LED = parse(tokenized_LED)
    compiled_LED_to_js = comp_func(pared_LED)
    return compiled_LED_to_js
