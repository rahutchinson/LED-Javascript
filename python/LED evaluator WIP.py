##LED evaluator based on AST provided by parsing
##@Author: Roger Campbell


##Containers
##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
#['cons','nil']['cons', obj, 'nil'] | ['cons', obj, cons]
def cons(L):
    if L[1]=='nil':
        return []
    elif L[2]=='nil':
        return [L[1]]
    else:
        temp = [L[1]]
        temp2 = L[2]
        for i in range(0,len(temp2)):
            temp.append(temp2[i])
        return temp

##Set ::= { } | { Objs }
##['set'] -> {}
##['set', Objs] -> {Objs}
##['Set',cons]
def Set(L):
    return frozenset(L[1])
##Tup ::= ( Obj , Objs)
##['tup', Obj, Objs] -> (Obj, Objs)
def Tup(L):
    return tuple(L[1])

##Seq ::= < > | < Objs> 
## ['seq'] -> < >
## ['seq', Objs] -> <Objs>
def Seq(L):
    return L
##Arithmetic

##exponentiation
##['exp',t1,t2] -> t1^t2
def Exp(L):
    return L[1] ^ L[2]

##unary increment
##['inc',t1] -> +t1
def Inc(L):
    return L[1]+1

##unary decrement
##['dec',t1] -> -t1
def Dec(L):
    return L[1]-1

##multiplication
##['mul',t1,t2] -> t1 * t2
def Mul(L):
    return L[1]*L[2]

##division
##['div',t1,t2] -> t1 / t2
def Div(L):
    return L[1]/L[2]

##addition
##['add',t1,t2] -> t1 + t2
def Add(L):
    return L[1]+L[2]

##subtraction
##['sub',t1,t2] -> t1 - t2
def Sub(L):
    return L[1]-L[2]


##Sets

##set product
##['setProd', t1, t2] -> t1 * t2 #t1,t2 are sets
def SetProd(L):
    return set((a,b) for a in L[1] for b in L[2])
##sec
##['sec', t1, t2] -> t1 sec t2
def Sec(L):
    return false

##union
##['union', t1, t2] -> t1 U t2
def Union(L):
    return frozenset(L[1].union(L[2]))

##set Diff
##['setDiff', t1, t2] -> t1 / t2
def SetDiff(L):
    return L[1]-L[2]


##Conditionals

##Less than
##['<', t1, t2] -> t1 < t2
def LT(L):
    return L[1] < L[2]

##Greater than
##['>', t1, t2] -> t1 > t2
def GT(L):
    return L[1] > L[2]

##Less than or equal to
##['<=', t1, t2] -> t1 <= t2
def LTE(L):
    return L[1] <= L[2]

##Greater than or equal to
##['>=', t1, t2] -> t1 >= t2
def GTE(L):
    return L[1] >= L[2]

##Equal to
##['=', t1, t2] -> t1 = t2
def EQ(L):
    return L[1] == L[2]

##Contained in
##['in', t1, t2] -> t1 in t2 #t1 is an Obj t2 is a container
def In(L):
    return L[1] in L[2]

##subset
##['subSet', t1, t2] -> t1 sub t2 #t1 and t2 are sets
def SubSet(L):
    return L[1].issubset(L[2])

##Boolean Connectives

##not
##['not', t1] -> ~t1
def Not(L):
    return not L[1]

##and
##['and', t1, t2] -> t1 & t2
def And(L):
    return L[1] and L[2]

##or
##['or', t1, t2] -> t1 V t2
def Or(L):
    return L[1] or L[2]
        
##implication
##['imp', t1, t2] -> t1 => t2
def Imp(L):
    return not L[1] or L[2]
        
##if and only if
##['iff', t1, t2] -> t1 <=> t2
def Iff(L):
    return (L[1] and L[2]) or (not L[1] and not L[2])

def evaluate(L):
    f = globals()["%s" % L[0]]
    print(f)
    if len(L)>= 2 and isinstance(L[1],list):
        L[1]=evaluate(L[1])
    if len(L)>= 3 and isinstance(L[2],list):
        L[2]=evaluate(L[2])
    return f(L)
#print(evaluate(['Set', ['cons', 1, ['cons', ['Set', ['cons', 2, ['cons', 3, 'nil']]], ['cons', 4, 'nil']]]]))
#print(evaluate(['Union', ['Set', ['cons', 1, ['cons', 2, ['cons', ['Add', 3, 4], 'nil']]]], ['Set', ['cons', ['Imp', True, False], ['cons', 7, 'nil']]]]))

