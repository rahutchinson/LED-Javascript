##LED evaluator based on AST provided by parsing
##@Author: Roger Campbell

def comp_func(L):
    output = ''
    for definition in L:
        output.append( "function "+L[0]+'('+L[1]+')'+'{'+'\nreturn'+evaluate(L[2])+'\n}\n')
    return output

##Containers
##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas
# ['cons','nil']['cons', obj, 'nil'] | ['cons', obj, cons]
def cons(L):
    if L[1] == 'nil':
        return ""
    elif L[2] == 'nil':
        return str(L[1])
    else:
        return str(L[1])+','+str(L[2])


##Set ::= { } | { Objs }
##['set'] -> {}
##['set', Objs] -> {Objs}
##['Set',cons]
def Set(L):
    return "toSet(" +'[' + L[1] + ']'+ ")"


##Tup ::= ( Obj , Objs)
##['tup', Obj, Objs] -> (Obj, Objs)
def Tup(L):
    return "Tup("+'['+L[1]+']'+')'


##Seq ::= < > | < Objs>
## ['seq'] -> < >
## ['seq', Objs] -> <Objs>
def Seq(L):
    return "Seq("+'['+ L[1] +']'+")"


##Arithmetic

##exponentiation
##['exp',t1,t2] -> t1^t2
def Exp(L):
    return L[1] ^ L[2]
    return '(' + str(L[1]) + '^' + str(L[2]) + ')'


##unary increment
##['inc',t1] -> +t1
def Inc(L):
    return '(' + str(L[1]) + '+ 1)'


##unary decrement
##['dec',t1] -> -t1
def Dec(L):
    return '(' + str(L[1]) + '- 1)'


##multiplication
##['mul',t1,t2] -> t1 * t2
def Mul(L):
    return '(' + str(L[1]) + '*' + str(L[2]) + ')'


##division
##['div',t1,t2] -> t1 / t2
def Div(L):
    return '(' + str(L[1]) + '/' + str(L[2]) + ')'


##addition
##['add',t1,t2] -> t1 + t2
def Add(L):
    return '(' + str(L[1]) + "+" + str(L[2]) + ')'


##subtraction
##['sub',t1,t2] -> t1 - t2
def Sub(L):
    return '(' + str(L[1]) + '-' + str(L[2]) + ')'


##Sets

##set product
##['setProd', t1, t2] -> t1 * t2 #t1,t2 are sets
def SetProd(L):
    #return set((a, b) for a in L[1] for b in L[2])
    return "cross(" + L[1] + ',' + L[2] + ')'

##sec
##['sec', t1, t2] -> t1 sec t2
def Sec(L):
    return "intersect(" + L[1] + ',' + L[2] + ')'


##union
##['union', t1, t2] -> t1 U t2
def Union(L):
    return "union(" + str(L[1]) + "," + str(L[2]) + ")"


##set Diff
##['setDiff', t1, t2] -> t1 / t2
def SetDiff(L):
    return "setDiff("+L[1]+',' + L[2]+')'


##Conditionals

##Less than
##['<', t1, t2] -> t1 < t2
def LT(L):
    return '(' + str(L[1]) + '<' + str(L[2]) + ')'


##Greater than
##['>', t1, t2] -> t1 > t2
def GT(L):
    return '(' + str(L[1]) + '>' + str(L[2]) + ')'


##Less than or equal to
##['<=', t1, t2] -> t1 <= t2
def LTE(L):
    return '(' + str(L[1]) + '<=' + str(L[2]) + ')'


##Greater than or equal to
##['>=', t1, t2] -> t1 >= t2
def GTE(L):
    return '(' + str(L[1]) + '>=' + str(L[2]) + ')'


##Equal to
##['=', t1, t2] -> t1 = t2
def EQ(L):
    return '(' + str(L[1]) + '==' + str(L[2]) + ')'


##Contained in
##['in', t1, t2] -> t1 in t2 #t1 is an Obj t2 is a container
def In(L):
    return "inSet(" + L[1] + ',' + L[2] + ')'


##subset
##['subSet', t1, t2] -> t1 sub t2 #t1 and t2 are sets
def SubSet(L):
    return "isSubset("+L[1]+','+L[2]+')'


##Boolean Connectives

##not
##['not', t1] -> ~t1
def Not(L):
    return '!'+str(L[1]).lower()


##and
##['and', t1, t2] -> t1 & t2
def And(L):
    return str(L[1]).lower()+'&&'+str(L[2]).lower()


##or
##['or', t1, t2] -> t1 V t2
def Or(L):
    return str(L[1]).lower()+'||'+str(L[2]).lower()


##implication
##['imp', t1, t2] -> t1 => t2
def Imp(L):
    return '!' + str(L[1]).lower() + '||' + str(L[2]).lower()


##if and only if
##['iff', t1, t2] -> t1 <=> t2
def Iff(L):
    return '('+str(L[1]).lower()+'&&'+str(L[2]).lower()+')'+ '||' +'('+'!'+str(L[1]).lower()+'&&'+'!'+str(L[2]).lower()+')'


def evaluate(L):
    f = globals()["%s" % L[0]]
    print(f)
    if len(L) >= 2 and isinstance(L[1], list):
        L[1] = evaluate(L[1])
    if len(L) >= 3 and isinstance(L[2], list):
        L[2] = evaluate(L[2])
    return f(L)