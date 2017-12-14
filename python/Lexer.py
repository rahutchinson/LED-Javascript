'''
Finite state machine tokenizer
(c) Nelson Rushton, Texas Tech CS
March 2017
'''

# whiteChar(c) iff c is a whitespace character.
def whiteChar(c): return (c in " \r\n\t\v")

# tokenize(s) = Tokenize(s), whenever Tokenize(s) is defined
def lex(s):
  i = 0 
  tokens = [ ]
  # invariants:0 <= i <= len(s),  tokens = Tokenize(s[:i]),
  while i < len(s):
    if whiteChar(s[i]): 
      i = i+1
    elif i < len(s)-1 and s[i:i+2] == "//":
      # skip the comment until the next return or new line character
      i = i+2
      while i < len(s) and s[i] not in "\r\n": 
        i = i+1
    else: 
      # process the longest possible token
      tok = munch(s,i)
      tokens.append(tok)
      i = i + len(tok)
  return tokens

 
# If 0<= i < len(s) and s[i:] begins with a token, then munch(s,i)
# is longest token that is a prefix of s[i:]

def munch(s,i):
  A,j = 'em',i
  # invariants: i <= j <= len(s), A is the state that describes s[i:j] 
  while True:
    if j == len(s): break # end of string
    A = newState(A,s[j])
    # A is now the state that *would* result if we process
    # one more character. 
    if A == 'err': break
    # A is not 'err', so good with one more character
    j = j+1 
  return s[i:j]
  


'''
A *state* is a string . States *describe* strings as given below:

1. 'em' describes str iff str is empty
2. 'id' describes str iff str is an identifier
3. 'num' describes str iff is a numeral
4. 'err' describes str iff str is not a prefix of any token
'''
# If state A describes a string and c is a character, than newState(A,c)
# describes the string A+c.

def isSpecial(c):
    return c in "<>=*+-^|,~.{}()[]\/&:;$"


def newState(A,c):
    if  A=='em':
        if c.isalpha() or c == '`': return 'id'
        elif c.isdigit(): return 'num'
        elif c == '"': return 'str'
        # elif c == "(": return 'left_paren'
        elif c == ".": return 'period'
        elif isSpecial(c):
            if c == '<': return '<_extendable'
            elif c == '>': return '>_extendable'
            elif c == '=': return '=_extendable'
            elif c == ':': return ':_extendable'
            else: return 'non-extendable'
    elif A=='id':
        if (c.isalpha() or c.isdigit() or c == '_'): return 'id'
    elif A == 'num':
        if c.isdigit(): return 'num'
        elif c == "(": return 'left_paren'
        elif c == ".": return 'period'
    elif A == 'str':
        if c == "'": return 'end_str'
        else: return 'str'
    elif A == 'left_paren':
        if c.isdigit(): return 'repeat_dig'
    elif A == 'period':
        if c.isdigit(): return 'decimal'
        if c == '(': return 'left_paren'
        if c == '.': return '.._end'
    elif A == 'decimal':
        if c.isdigit(): return 'decimal'
        if c == '(': return 'left_paren'
    elif A == 'repeat_dig':
        if c.isdigit(): return 'repeat_dig'
        elif c == '.': return 'repeat_1.'
    elif A == 'repeat_1.':
        if c == '.': return 'repeat_2.'
    elif A == 'repeat_2.':
        if c == ')': return 'end_repeat'
    elif A == '<_extendable':
        if c == '=': return '<=_extendable'
    elif A == '>_extendable':
        if c == '=': return 'non-extendable'
    elif A == '<=_extendable':
        if c == '>': return 'non-extendable'
    elif A == ':_extendable':
        if c == '=': return 'non-extendable'
    
    return 'err'


def open_LED_file(filename):
    with open(filename, "r") as file:
        s = file.read()
    return s


def preprocess_codeblocks(file):
    code_block = False

    code_array = []
    code_string = ''
    last_char = None
    for char in file:

        if last_char:
            if last_char=='/' and char == '$':
                code_block = True
            if last_char=='$' and char == '/':
                code_block = False
                code_array += [code_string[1:-2]]
                code_string = ''
            if code_block:
                code_string += char

        last_char = char
    return ''.join(code_array).replace('\n',' ')


def preprocess_definitions(token_array):
    list_of_definitions = []
    tokens_in_buffer = []
    current_def = []
    last_token = ' '
    paren_open = False
    for token in token_array:

        if last_token[0].isalpha() and last_token != 'iff' and token == "(":
            paren_open = True
            tokens_in_buffer += [token]

        elif paren_open and last_token == ")" and token in ["iff",":="]:
            #print("Found def")
            paren_open = False
            list_of_definitions += [current_def]
            current_def = tokens_in_buffer
            tokens_in_buffer = []

        elif last_token[0].isalpha() and token in ["iff",":="]:
            #print("Found def",last_token,token)
            paren_open = False
            list_of_definitions += [current_def]
            current_def = [last_token]
            tokens_in_buffer = []


        elif paren_open and last_token == ")" and token not in ["iff",":="]:
            current_def += tokens_in_buffer
            tokens_in_buffer = []
            paren_open = False

        elif paren_open:
            tokens_in_buffer += [token]

        elif token[0].isalpha() and not paren_open:
            current_def += [last_token]
            tokens_in_buffer = [token]

        else:
            current_def += [last_token]
            tokens_in_buffer = []

        last_token = token
    if current_def != []:
        list_of_definitions += [current_def]
    for defi in list_of_definitions:
        if ":=" in defi or "iff" in defi:
            pass
        else:
            list_of_definitions.remove(defi)
    return list_of_definitions



# print(lex("alpha := lambda x: x + 5"))
# END PROGRAM

#print(lex(preprocess_codeblocks(open_LED_file("TicTacToe"))))
#print(preprocess_definitions(lex(preprocess_codeblocks(open_LED_file("TicTacToe")))))
