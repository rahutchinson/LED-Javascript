from python.Lexer import *
from python.Tokenizer import *
from python.LED_GameParser import *
from python.LED_GameCompiler_js import *
import os
import shutil




# This function is used for debugging purposes and will print the results of intermediate functions
def compile_LED_to_JS(LED_code_string):
    LED_code = preprocess_codeblocks(LED_code_string)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    print("TOKENIZED")
    print(tokenized_LED)
    pared_LED = parse(tokenized_LED)
    print("PARSED")
    print(pared_LED)
    print('\n')
    compiled_LED_to_js = comp_func(pared_LED)

    return compiled_LED_to_js

def compile_LED_file_to_JS(filename):

    helper_js_string = open_file_as_string("../js/helpers.js")

    LED_code_string = open_file_as_string(filename)
    LED_code = preprocess_codeblocks(LED_code_string)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    pared_LED = parse(tokenized_LED)
    compiled_LED_to_js = comp_func(pared_LED)
    compiled_LED_with_helpers = compiled_LED_to_js + helper_js_string

    return compiled_LED_with_helpers

def LED_to_EASEL_game(filename):

    EASEL_code = open_file_as_string("../js/EaselJS.js")
    HTML_code = open_file_as_string("HTML_main.html")

    if not os.path.exists("LED_Game"):
        os.makedirs("LED_Game")
    else:
        shutil.rmtree('LED_Game')
        os.makedirs("LED_Game")


    compiled_LED_to_js = compile_LED_file_to_JS(filename)

    JS_file = open("LED_Game/JS_code.js", "w+")
    for i in compiled_LED_to_js: JS_file.write(i)
    JS_file.close()

    EASEL_file = open("LED_Game/Easel_Game_Engine.js", "w+")
    for i in EASEL_code: EASEL_file.write(i)
    EASEL_file.close()

    HTML_file = open("LED_Game/HTML_file.html", "w+")
    for i in HTML_code: HTML_file.write(i)
    HTML_file.close()

    return ("Created game")


print(LED_to_EASEL_game("NaughtsAndCrossesTrue"))

#print(compile_LED_to_JS("/$ newDef(s) := s + 10 $/"))
