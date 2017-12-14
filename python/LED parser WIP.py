# A program to parse LED to AST notation
# Author: Roger W. Campbell

##Based upon the following grammar:
##Obj ::= T4 | B5 | Cont | Str | Func  /* Added by Beau */
##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
##Cont ::= Set | Tup | Seq
##Set ::= { } | { Objs }
##Tup ::= ( Obj , Objs)
##Seq ::= < > | < objs>
##
##Func ::= lambda Objs :
##Func ::= identifier cont := Objs | identifier := Objs
##
##T0 ::= intNum | (  T4   )
##T1 ::= T0 | T0 ^ T1
##T2 ::= T1 | + T2 | - T2 | f T2
##T3 ::= T2 | T3 * T2 | T3 / T2
##T4 ::= T3 | T4 + T3 | T4 - T3
##
##S0 ::= Set | ( S2 )
##S1 ::= S0 | S1 * S0 | S1 sec S0
##S2 ::= S1 | S2 U S1 | S2 / S1
##
##Cond ::= T4 < T4 | T4 > T4 | T4 = T4 | T4 <= T4 | T4 >= T4 | Obj in S2 | S2 sub S2
##
##Quant ::=  some Obj in T4. B5 | all Obj in T4. B5
##
##B0 ::= Boolean | ( B5 ) | Cond
##B1 ::= B0 | ~B1
##B2 ::= B1 | B2 & B1
##B3 ::= B2 | B3 V B2
##B4 ::= B3 | B4 => B3
##B5 ::= B4 | B5 <=> B4

def parse(L):
    (flag, tree)= Objs(L)
    if flag:
        return tree
    else:
        return None


def ContPair(open,close):
    if open == '{' and close == '}' or open == '(' and close == ')' or open == '<' and close == '>':
        return True
    else:
        return False

'''
def parseLHS(S):
    if len(S)==1 and isIdentifier(S[0]):
        return ((S[0],[]),True)
    if isIdentifier(S[0]) and S[1]=='(' and S[len(S)-1]==')':
        fName = S[0] # the name of the function
        # f()
        if len(S)==3:
            return ((fName,[]),True)
        t,f = parseTerms(S[2:-1])
        if f:
            S = S[2:len(S)-1]
            fParams = params(S)
            return ((fName,fParams),True)
    return (None,False)
 

# rule: funcBody -> Expression | conditional
def parseFuncBody(S):
    tree1,flag1 = parseConditional(S)
    if flag1:
        return (tree1,True)
    tree2,flag2 = parseExpression(S)
    if flag2:
        return (tree2,True)
    return (None,False)

# rule: conditional -> ifClauses | ifClauses ; term otherwise
def parseConditional(S):
    if S[-1]=='otherwise':
        S = S[:-1]
        # find the last ';' of S
        i = lastIndex(';',S)
        (t2,f2)=parseIfClauses(S[0:i])
        (t1,f1)= parseTerm(S[i+1:])
        if f1 and f2: 
            if(t2.op()=='cond'):
                # add otherwise to the list of AST
                return (AST('cond',t2.args()+[AST('ow',[t1])]),True) 
            else:
                return (AST('cond',[t2,AST('ow',[t1])]),True) 

    tree1,flag1 = parseIfClauses(S)
    if flag1:
        return (tree1,True) 
    return (None,False)    

# rule: ifClasuses -> ifClause | ifClause ; ifClauses
def parseIfClauses(S):
    for i in range(len(S)):
        if S[i]==';':
            (t1,f1)=parseIfClause(S[0:i])
            (t2,f2)= parseIfClauses(S[i+1:])
            if f1 and f2: 
                if(isinstance(t2.tree,list) and t2.op()=='cond'):
                    return (AST('cond',[t1]+t2.args()),True) 
                else:
                    return (AST('cond',[t1,t2]),True)
    (tree,flag) = parseIfClause(S)
    if flag: 
        return (tree,True)    
    return (None,False)    

# rule: ifClause -> term if statement
def parseIfClause(S):
    for i in range(len(S)):
        if S[i]=='if':
            (t1,f1)=parseTerm(S[0:i])
            # statement and sentence are used interchangely 
            (t2,f2)= parseSentence(S[i+1:])
            if f1 and f2: 
                return (AST('if',[t2,t1]),True) 
    return (None,False)    

def parseWhereClause(S):
    #rule: whereClause -> where Stmt
    
    if len(S)>1 and S[0]=='where':
        (t,f)=parseSentence(S[1:])
        if f:
            return (t,True)
    return(None,False)
'''
'''

# helper function
# str * list<str> -> int
# If C is a string and S is a list of string, lastIndex(C, S) is the index of the last C in S if there is at least C,
# otherwise lastIndex(C, S) = 0

def lastIndex(C, S):
    index = 0
    for i in range(len(S)):
        if(S[i]==C):
            index = i
    return index
            
            
# Expression -> Sentence | Term
def parseExpression(S):
    if S==None or len(S)==0:
        return(None,False)
    tree2,flag2 = parseSentence(S)
    if flag2:
        return (tree2,True)
    tree1,flag1 = parseTerm(S)
    if flag1:
        return (tree1,True)
    return (None,False)

# rule: Sentence -> S6 | ( S6 )
def parseSentence(S):
    if S==None or len(S)==0:
        return(None,False)
    tree2,flag2 = parseS6(S)
    if flag2:
        return (tree2,True)
    if S[0]=='(' and S[-1]==')':
        tree1,flag1 = parseS6(S[1:-1])
        if flag1:
            return (tree1,True)
    return (None,False)
'''

'''
# rule: some  var  in  term . S2 | all   var  in  term . S2
def parseSomeAll(S):
    separators = ['some','all']
    if len(S)<6:
        return(None,False)
    if S[0] in separators:
        try:
            i = S.index('in')
            j = S.index('.')
            t1,f1 = parseVar(S[1])
            t2,f2 = parseTerm(S[i+1:j])
            t3,f3 = parseS2(S[j+1:])
            if f1 and f2 and f3:
                return (AST(S[0],[t1,t2,t3]),True)
        except ValueError:
            return (None,False)
    return (None,False)
    
    def universalParse(S,F):
    helper function to remove duplicate functions
    list<list<str>> * list<str> -> tuple
    If S is a list of parsing list of string, and F is a list of parsing functions
    then universalParse(S,F) = (trees,True), where trees is a list of the abstract syntax trees,
    if each memeber of S complies to its corresponding rule in F
    otherwise universalParse(S,F) = (None,False). 
    For example, if S = [['Int'],['Int']], F=['TExp0','TExp0'] then universalParse(S,F)= (trees,True), 
    where trees=[t1,t2] and t1 is AST of parseTExp0(S[0]) and t2 is the AST of parseTExp0(S[1])
    
    trees = []
    flags = []
    if len(F)>0 and len(F) ==len(S):
        for i in range(len(F)):
            func = functionNames(F[i])
            t,f = func(S[i])
            trees.append(t)
            flags.append(f)
        if all(flags):
            return (trees,True)
    return (None,False)
'''
##Cont ::= Set | Tup | Seq
##list<tokens> -> bool*AST
def Cont(L):
    (flag, tree) = Set(L)
    if flag: return (True, tree)
    (flag, tree) = Tup(L)
    if flag: return (True, tree)
    (flag, tree) = Seq(L)
    if flag: return (True, tree)

    return (False, None)



def Set(L):
    #check for multiple separate sets as in the case of S2
    stack = []
    for i in range(0, len(L)-1):
        if L[i] == '{':
            stack.append(L[i])
        elif L[i] == '}':
            stack.pop()

        if len(stack)==0:
            return (False,None)

    #proceeding once only one set is present
    if L[0]=='{' and L[-1]=='}':
        if len(L)==2:
            return (True,['Set',cons(None,None)])
        temp=L[1:-1]
        (nextEle, remains)=nextElement(temp)
        return (True, ['Set', cons(nextEle,remains)])
    else:
        return (False, None)

def cons(ele,L):
    if ele==None and L == None:
        return ['cons','nil']
    ele=Obj(ele)[1]
    if L==None:
        return ['cons', ele, 'nil']
    else:
        (nextEle, remains) = nextElement(L)
        return ['cons', ele, cons(nextEle,remains)]

def nextElement(L):
    stack=[]
    for i in range(0,len(L)):
        if L[i] in ['{','<','(']:
            stack.append(L[i])
        elif L[i] in ['}','>',')']:
            if not ContPair(stack.pop(),L[i]):
                return None,None
        if L[i]==',' and len(stack)==0:
            return (L[:i],L[i+1:])
    return L,None


##Tup ::= ( Obj , Objs)
##list<tokens> -> bool*AST
def Tup(L):
    if L[0]=='(' and L[-1]==')':
        if len(L)==2:
            return (False,None)
        temp=L[1:-1]
        (nextEle, remains)=nextElement(temp)
        if remains == None:
            return (False,None)
        return (True, ['Tup', cons(nextEle,remains)])
    else:
        return (False, None)
    # if L[0] == '(':
    #     (f1, t1) = Obj(L[1])
    #     (f2,t2) = Objs(L[2:len(L)-1])
    #     if f1 and f2 and L[len(L) - 1] == ')':
    #         return (True, ['Tup', t1, t2])
    #
    # return (False, None)


##Seq ::= < > | < Objs>
##list<tokens> -> bool*AST
def Seq(L):
    if L[0]=='<' and L[-1]=='>':
        if len(L)==2:
            return (True,['Seq',cons(None,None)])
        temp=L[1:-1]
        (nextEle, remains)=nextElement(temp)
        return (True, ['Seq', cons(nextEle,remains)])
    else:
        return (False, None)
    # #< >
    # if L[0] == '<':
    #     if L[1] == '>':
    #         return (True, ['<>'])
    #     #< Objs >
    #     else:
    #         (f1, t1) = Objs(L[1:len(L) - 1])
    #         if f1 and L[len(L) - 1] == '>':
    #             return (True, ['Seq', t1])
    # #error
    # return (False, None)


##Obj ::= T4 | B5 | Cont | Str
##list<tokens> -> bool*AST
def Obj(L):
    #T4
    (flag, tree) = T4(L)
    if flag: return (True, tree)
    #B5
    (flag, tree) = B5(L)
    if flag:
        return (True, tree)
    #S2
    (flag, tree) = S2(L)
    if flag: return (True, tree)
    #Cont
    (flag, tree) = Cont(L)
    if flag:
        return (True, tree)
    #Str
    elif len(L)==1 and isinstance(L[0], str):
        return (True, [L[0]])
    #error
    return (False, None)


##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
##list<tokens> -> bool*AST
def Objs(L):
    if len(L)==1:
        return Obj(L)
    else:
        (nextEle, remains) = nextElement(L)
        if remains == None:
            return Obj(nextEle)
        else:
            (flag, tree) = Obj(nextEle)
            if flag:
                return tree.append(Objs(remains))

    return (False,None)

    # trees = []
    # comaIndex = []
    # if len(L)==1:
    #     return Obj(L)
    # else:
    #     for i in range(0,len(L)):
    #         if L[i] == ',':
    #             comaIndex.append(i)
    #     for n in range(0, len(comaIndex)):
    #         if n == 0:
    #             trees.append(Obj(L[:comaIndex[n]])[1])
    #             trees.append(',')
    #         if n == len(comaIndex) - 1:
    #             trees.append(Obj(L[comaIndex[n] + 1:])[1])
    #         else:
    #             trees.append(Obj(L[comaIndex[n] + 1:comaIndex[n + 1]])[1])
    # if(len(comaIndex)==0):
    #     trees.append(Obj(L)[1])
    # if None in trees:
    #     return (False, None)
    # else:
    #     return(True,trees)




##
##T0 ::= Num | (  T4   )
##list<tokens> -> bool*AST
def T0(L):
    #Num
    if isinstance(L[0], (int, float, complex)) and len(L)==1: return (True, L[0])
    #(T4) test this may need to end range at len(L)-3
    if L[0] == '(':
        (f1, t1) = T4(L[1:-1])
        if f1 and L[-1] == ')':
            return (True, t1)
    #error
    return (False, None)


##T1 ::= T0 | T0 ^ T1
##list<tokens> -> bool*AST
def T1(L):
    # T0
    (flag, tree) = T0(L)
    if flag: return (True, tree)

    #T0 ^ T1
    for i in range(1, len(L) - 1):
        if L[i] == '^':
            (f1, t1) = T0(L[0:i])
            (f2, t2) = T1(L[i + 1:])
            if f1 and f2: return (True, ['Exp', t1, t2])

    #error
    return (False, None)


##T2 ::= T1 | + T2 | - T2 | f T2
##list<tokens> -> bool*AST
def T2(L):
    # T1
    (flag, tree) = T1(L)
    if flag: return (True, tree)

    #+ T2 | - T2 | f T2
        #+ T2
    if L[0] == '+':
        (f1, t1) = T2(L[1:])
        if f1: return (True, ['Inc', t1])
        #- T2
    elif L[0] == '-':
        (f1, t1) = T2(L[1:])
        if f1: return (True, ['Dec', t1])
        #f T2 undone return (True,['f',t1])


    return (False, None)


##T3 ::= T2 | T3 * T2 | T3 / T2
##list<tokens> -> bool*AST
def T3(L):
    # T2
    (flag, tree) = T2(L)
    if flag: return (True, tree)

    #T3 * T2 | T3 / T2
    for i in range(1, len(L) - 1):
        #T3 * T2
        if L[i] == '*':
            (f1, t1) = T3(L[0:i])
            (f2, t2) = T2(L[i + 1:])
            if f1 and f2: return (True, ['Mul', t1, t2])
        #T3 / T2
        elif L[i] == '/':
            (f1, t1) = T3(L[0:i])
            (f2, t2) = T2(L[i + 1:])
            if f1 and f2: return (True, ['Div', t1, t2])

    #error
    return (False, None)


##T4 ::= T3 | T4 + T3 | T4 - T3
##list<tokens> -> bool*AST
def T4(L):
    # T3
    (flag, tree) = T3(L)
    if flag: return (True, tree)

    #T4 + T3 | T4 - T3
    for i in range(1, len(L) - 1):
        #T4 + T3
        if L[i] == '+':
            (f1, t1) = T4(L[0:i])
            (f2, t2) = T3(L[i + 1:])
            if f1 and f2: return (True, ['Add', t1, t2])
        #T4 - T3
        elif L[i] == '-':
            (f1, t1) = T4(L[0:i])
            (f2, t2) = T3(L[i + 1:])
            if f1 and f2: return (True, ['Sub', t1, t2])

    #error
    return (False, None)


##S0 ::= Set | ( S2 )
##list<tokens> -> bool*AST
def S0(L):
    #Set
    (flag, tree) = Set(L)
    if flag: return (True, tree)
    #(S2)
    if L[0] == '(':
        (f1, t1) = S2(L[1:-1])
        if f1 and L[-1] == ')':
            return (True, t1)
    #error
    return (False, None)


##S1 ::= S0 | S1 * S0 | S1 sec S0
##list<tokens> -> bool*AST
def S1(L):
    # S0
    (flag, tree) = S0(L)
    if flag: return (True, tree)
    #S1 * S0 | S1 sec S0
    for i in range(1, len(L) - 1):
        #S1 * S0
        if L[i] == '*':
            (f1, t1) = S1(L[0:i])
            (f2, t2) = S0(L[i + 1:])
            if f1 and f2: return (True, ['setProd', t1, t2])
        #S1 sec S0
        elif L[i] == 'sec':
            (f1, t1) = S1(L[0:i])
            (f2, t2) = S0(L[i + 1:])
            if f1 and f2: return (True, ['Sec', t1, t2])
    #error
    return (False, None)


##S2 ::= S1 | S2 U S1 | S2 \ S1
##list<tokens> -> bool*AST
def S2(L):
    # S1
    (flag, tree) = S1(L)
    if flag: return (True, tree)
    #S2 U S1 | S2 \ S1
    for i in range(1, len(L) - 1):
        #S2 U S1
        if L[i] == 'U':
            (f1, t1) = S2(L[0:i])
            (f2, t2) = S1(L[i + 1:])
            if f1 and f2: return (True, ['Union', t1, t2])
        #S2 \ S1
        elif L[i] == '\\':
            (f1, t1) = S2(L[0:i])
            (f2, t2) = S1(L[i + 1:])
            if f1 and f2: return (True, ['setDiff', t1, t2])

    #error
    return (False, None)



##Cond ::= T4 < T4 | T4 > T4 | T4 = T4 | T4 <= T4 | T4 >= T4 | Obj in S2 | S2 sub S2
##list<tokens> -> bool*AST
def Cond(L):
    for i in range(1, len(L) - 1):
        #T4 < T4 | T4 > T4 | T4 = T4 | T4 <= T4 | T4 >= T4
        if L[i] in ['<', '>', '=', '<=', '>=']:
            expComp = L[i]
            (f1, t1) = T4(L[0:i])
            (f2, t2) = T4(L[i + 1:])
            if f1 and f2: return (True, [expComp, t1, t2])
        #Obj in S2
        elif L[i] == 'in':
            (f1, t1) = Obj(L[0:i])
            (f2, t2) = S2(L[i + 1:])
            if f1 and f2: return (True, ['In', t1, t2])
        #S2 sub S2
        elif L[i] == 'sub':
            (f1, t1) = S2(L[0:i])
            (f2, t2) = S2(L[i + 1:])
            if f1 and f2: return (True, ['subSet', t1, t2])
    #error
    return (False, None)


##Quant ::=  some Obj in S2. B5 | all Obj in S2. B5
##list<tokens> -> bool*AST
def Quant(L):

    return (False, None)


##B0 ::= Boolean | ( B5 ) | Cond
##list<tokens> -> bool*AST
def B0(L):
    #Boolean
    if isinstance(L[0], bool) and len(L)==1 : return (True, L[0])
    #( B5 )
    if L[0] == '(':
        (f1, t1) = B5(L[1:-1])
        if f1 and L[-1] == ')': return (True, t1)
    #Cond
    (flag, tree) = Cond(L)
    if flag: return (True, tree)
    #error
    return (False, None)


##B1 ::= B0 | ~B1
##list<tokens> -> bool*AST
def B1(L):
    # B0
    (flag, tree) = B0(L)
    if flag: return (True, tree)
    #~B1
    if L[0] == '~':
        (f1, t1) = B1(L[1:])
        if f1: return (True, ['Not', t1])

    #error
    return (False, None)


##B2 ::= B1 | B2 & B1
##list<tokens> -> bool*AST
def B2(L):
    #B1
    (flag, tree) = B1(L)
    if flag: return (True, tree)
    #B2 & B1
    for i in range(1, len(L) - 1):
        if L[i] == '&':
            (f1, t1) = B2(L[0:i])
            (f2, t2) = B1(L[i + 1:])
            if f1 and f2: return (True, ['And', t1, t2])

    #error
    return (False, None)


##B3 ::= B2 | B3 V B2
##list<tokens> -> bool*AST
def B3(L):
    # B2
    (flag, tree) = B2(L)
    if flag: return (True, tree)
    #B3 V B2
    for i in range(1, len(L) - 1):
        if L[i] == 'V':
            (f1, t1) = B3(L[0:i])
            (f2, t2) = B2(L[i + 1:])
            if f1 and f2: return (True, ['Or', t1, t2])

    #error
    return (False, None)


##B4 ::= B3 | B4 => B3
##list<tokens> -> bool*AST
def B4(L):
    # B3
    (flag, tree) = B3(L)
    if flag: return (True, tree)
    #B4 => B3
    for i in range(1, len(L) - 1):
        if L[i] == '=>':
            (f1, t1) = B4(L[0:i])
            (f2, t2) = B3(L[i + 1:])
            if f1 and f2: return (True, ['Imp', t1, t2])

    #error
    return (False, None)


##B5 ::= B4 | B5 <=> B4
##list<tokens> -> bool*AST
def B5(L):
    # B4
    (flag, tree) = B4(L)
    if flag: return (True, tree)
    #B5 <=> B4
    for i in range(1, len(L) - 1):
        if L[i] == '<=>':
            (f1, t1) = B5(L[0:i])
            (f2, t2) = B4(L[i + 1:])
            if f1 and f2: return (True, ['Iff', t1, t2])

    #error
    return (False, None)

#print(parse(['(',5,')']))
#print(parse(['(',1,'+',2,')']))
#print(parse(['<',1,'+',3,',','{',2,',',3,'}',',',4,'>']))
#print(parse(['{',1,',',2,',','(',3,'+',4,')','}','U','{','(',True,'=>',False,')',',',7,'}']))
#print(parse(['{',1,',','{',2,',',3,'}',',',4,'}']))
#print(parse([2, '+', 2, '^', '(', 4, '-', 4, '/', 5, ')', '-', '(', 18, '^', 1, '/', 5, ')']))