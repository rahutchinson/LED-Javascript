#A program to parse LED to AST notation
#Author: Roger W. Campbell

##lex = ''
##i=0;
##L=[F,->,T]
##
##def get():
##    global i
##    global L
##    temp = L[i]
##    i++
##    return temp
##
##def main():
##    global lex
##    lex=get()
##

##Based upon the following grammar:
##Cont ::= Set | Tup | Seq
##Set ::= { } | { Objs }
##Tup ::= ( Obj , Objs)
##Seq ::= < > | < objs> 
##Obj ::= T4 | B5 | Cont | Str
##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
##
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



##Cont ::= Set | Tup | Seq
##list<tokens> -> bool*AST
def cont(L):
    (flag, tree)= Set(L)
    if flag: return (true, tree)
    (flag, tree)= Tup(L)
    if flag: return (true, tree)
    (flag, tree)= Seq(L)
    if flag: return (true, tree)
    
    return (false, None)

##Set ::= { } | { Objs }
##list<tokens> -> bool*AST
def Set(L):
    for i in range(0,len(L)-2):
        if L[i]=='{':
            if L[i+1]=='}':
                return (true, ['{}'])
            else:
                (f1,t1)=Objs(L[i+1:len(L)-2])
                if f1 and L[len(L)-1]=='}':
                    return (true, ['set',t1])
                
    return (false, None)

##Tup ::= ( Obj , Objs)
##list<tokens> -> bool*AST
def Tup(L):
    return ( false, None)

##Seq ::= < > | < objs>
##list<tokens> -> bool*AST
def Seq(L):
    return ( false, None)

##Obj ::= T4 | B5 | Cont | Str
##list<tokens> -> bool*AST
def Obj(L):
    return ( false, None)

##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
##list<tokens> -> bool*AST
def Objs(L):
    return ( false, None)

##
##T0 ::= intNum | (  T4   )
##list<tokens> -> bool*AST
def T0(L):
    if isinstance(L[0], (int, long, float, complex)): return (true, L[0])
    
    #test this may need to end range at len(L)-3
    for i in range(0, len(L)-2):
        if L[i]=='(':
            (f1,t1)=T4(L[i+1:len(L)-2])
            if f1 and L[len(L)-1]==')':
                return (true, t1)
            
    return ( false, None)

##T1 ::= T0 | T0 ^ T1
##list<tokens> -> bool*AST
def T1(L):
    (flag,tree)=T0(L)
    if flag: return(true, tree)

    for i in range(1, len(L)-2):
        if L[i]=='^':
            (f1,t1)=T0(L[0:i])
            (f2,t2)=T1(L[i+1:])
            if f1 and f2: return (true,['exp',t1,t2])
    
    return ( false, None)

##T2 ::= T1 | + T2 | - T2 | f T2
##list<tokens> -> bool*AST
def T2(L):
    (flag,tree)=T1(L)
    if flag: return (true, tree)

    for i in range(0, len(L)-2):
        if L[i]=='+':
            (f1,t1)=T2(L[i+1:])
            if f1: return (true,['inc',t1])
        elif L[i]=='-':
            (f1,t1)=T2(L[i+1:])
            if f1 : return (true,['dec',t1])
        #f undone return (true,['f',t1])
    return ( false, None)

##T3 ::= T2 | T3 * T2 | T3 / T2
##list<tokens> -> bool*AST
def T3(L):
    (flag,tree)=T2(L)
    if flag: return (true, tree)

    for i in range(1, len(L)-2):
        if L[i]=='*':
            (f1,t1)=T3(L[0:i])
            (f2,t2)=T2(L[i+1:])
            if f1 and f2: return (true,['mul',t1,t2])
        elif L[i]=='/':
            (f1,t1)=T3(L[0:i])
            (f2,t2)=T2(L[i+1:])
            if f1 and f2: return (true,['div',t1,t2])
            
    return ( false, None)

##T4 ::= T3 | T4 + T3 | T4 - T3
##list<tokens> -> bool*AST
def T4(L):
    (flag,tree) = T3(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='+':
            (f1,t1)=T4(L[0:i])
            (f2,t2)=T3(L[i+1:])
            if f1 and f2: return (true,['add',t1,t2])
        elif L[i]=='-':
            (f1,t1)=T4(L[0:i])
            (f2,t2)=T3(L[i+1:])
            if f1 and f2: return (true,['sub',t1,t2])

    return (false, None)

##S0 ::= Set | ( S2 )
##list<tokens> -> bool*AST
def S0(L):
    (flag,tree)= Set(L)
    if flag: return(true,tree)

    for i in range(0, len(L)-2):
        if L[i]=='(':
            (f1,t1)=S2(L[i+1:len(L)-2])
            if f1 and L[len(L)-1]==')':
                return (true, t1)
    return ( false, None)

##S1 ::= S0 | S1 * S0 | S1 sec S0
##list<tokens> -> bool*AST
def S1(L):
    (flag,tree) = S0(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='*':
            (f1,t1)=S1(L[0:i])
            (f2,t2)=S0(L[i+1:])
            if f1 and f2: return (true,['setProd',t1,t2])
        elif L[i]=='sec':
            (f1,t1)=S1(L[0:i])
            (f2,t2)=S0(L[i+1:])
            if f1 and f2: return (true,['sec',t1,t2])
    return ( false, None)

##S2 ::= S1 | S2 U S1 | S2 \ S1
##list<tokens> -> bool*AST
def S2(L):
    (flag,tree) = S1(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='U':
            (f1,t1)=S2(L[0:i])
            (f2,t2)=S1(L[i+1:])
            if f1 and f2: return (true,['union',t1,t2])
        elif L[i]=='\':
            (f1,t1)=S2(L[0:i])
            (f2,t2)=S1(L[i+1:])
            if f1 and f2: return (true,['setDiff',t1,t2])

    return ( false, None)

##

##Cond ::= T4 < T4 | T4 > T4 | T4 = T4 | T4 <= T4 | T4 >= T4 | Obj in S2 | S2 sub S2
##list<tokens> -> bool*AST
def Cond(L):
    for i in range(1, len(L)-2):
        if L[i] in ['<','>','=','<=','>=']:
            expComp = L[i]
            (f1,t1)=T4(L[0:i])
            (f2,t2)=T4(L[i+1:])
            if f1 and f2: return(true,[expComp,t1,t2])
        elif L[i]=='in':
            (f1,t1)=Obj(L[0:i])
            (f2,t2)=S2(L[i+1:])
            if f1 and f2: return(true,['in',t1,t2])
        elif L[i]=='sub':
            (f1,t1)=S2(L[0:i])
            (f2,t2)=S2(L[i+1:])
            if f1 and f2: return(true,['sub',t1,t2])
    return ( false, None)

##Quant ::=  some Obj in S2. B5 | all Obj in S2. B5
##list<tokens> -> bool*AST
def Quant(L):
    return ( false, None)

##B0 ::= Boolean | ( B5 ) | Cond
##list<tokens> -> bool*AST
def B0(L):
    if isinstance(L[0], bool): return (true,L[0])

    (flag,tree)=Cond(L)
    if flag: return (true, tree)
    for i in range(0,len(L)-2):
        if L[i]=='(':
            (f1,t1)=B5(L[i+1:len(L)-2])
            if f1 and L[len(L)-1]==')': return (true,t1)
    return ( false, None)

##B1 ::= B0 | ~B1
##list<tokens> -> bool*AST
def B1(L):
    (flag,tree) = B0(L)
    if flag: return (true,tree)

    for i in range(0,len(L)-2):
        if L[i]=='~':
            (f1,t1)=B1(L[i+1:])
            if f1: return (true,['not',t1])
    return ( false, None)

##B2 ::= B1 | B2 & B1
##list<tokens> -> bool*AST
def B2(L):
    (flag,tree) = B1(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='&':
            (f1,t1)=B2(L[0:i])
            (f2,t2)=B1(L[i+1:])
            if f1 and f2: return (true,['and',t1,t2])
    return ( false, None)

##B3 ::= B2 | B3 V B2
##list<tokens> -> bool*AST
def B3(L):
    (flag,tree) = B2(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='V':
            (f1,t1)=B3(L[0:i])
            (f2,t2)=B2(L[i+1:])
            if f1 and f2: return (true,['or',t1,t2])
    return ( false, None)

##B4 ::= B3 | B4 => B3
##list<tokens> -> bool*AST
def B4(L):
    (flag,tree) = B3(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='=>':
            (f1,t1)=B4(L[0:i])
            (f2,t2)=B3(L[i+1:])
            if f1 and f2: return (true,['imp',t1,t2])
    return ( false, None)

##B5 ::= B4 | B5 <=> B4
##list<tokens> -> bool*AST
def B5(L):
    (flag,tree) = B4(L)
    if flag: return (true,tree)

    for i in range(1,len(L)-2):
        if L[i]=='<=>':
            (f1,t1)=B5(L[0:i])
            (f2,t2)=B4(L[i+1:])
            if f1 and f2: return (true,['iff',t1,t2])
        
    return ( false, None)
