from python.Lexer import *
from python.Tokenizer import *
from python.LED_GameParser import *
from python.LED_GameCompiler_js import *



FILENAME = "TicTacToe"

'''
def main():
    LED_file = open_LED_file(FILENAME)
    LED_code = preprocess_codeblocks(LED_file)
    lexed_LED = lex(LED_code)
    preprocessed_defs_LED = preprocess_definitions(lexed_LED)
    tokenized_LED = tokenize(preprocessed_defs_LED)
    pared_LED = parse(tokenized_LED)
    compiled_LED_to_js = comp_func(pared_LED)
    return compiled_LED_to_js
'''

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

#print(compile_LED_to_JS("/$ newState := segment(point(1,2),point(3,4),BLACK) $/"))
#print(compile_LED_to_JS("/$ legalToMoveIn(c) iff ~occupied(c) & ~gameOver $/"))

#print(compile_LED_to_JS("/$ even(n) iff `x $/"))

#print(compile_LED_to_JS("/$ playerToMove := `x if even(|currentState|); `o otherwise $/"))

#print(compile_LED_to_JS("/$ x := <L1> where L1 = segment(point(100,100),point(200,200),BLACK) $/"))

#print(compile_LED_to_JS('/$ initialState := < "0" > $/'))

"""
print(compile_LED_to_JS('''/$ 

                          displayImages(S) := square0 if S = "0"; 
                                                square1 if S = 1; 
                                                square2 if S = 2; 
                                                square3 if S = 3; 
                                                square4 if S = 4;
                                                empty otherwise
                                                
                        $/
                        '''))
"""

print(compile_LED_to_JS('''/$
cellClicked(c) iff
  mouseClicked &
  mouseX > xMin(c) 
$/'''))

    #legalToMoveIn(c) iff ~occupied(c) & ~gameOver

'''
function displayImages(S){
  
  if(S == '0'){
    return(square0());
  }
  else if(S == '1'){
    return(square1());
  }
  else if(S == '2'){
    return(square2());
  }
  else if(S == '3'){
    return(square3());
  }
  else if(S == '4'){
    return(square4());
  }
  return([[]]);
}


'''