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
    print(tokenized_LED)
    print(pared_LED)


main()