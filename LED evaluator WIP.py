##LED evaluator based on AST provided by parsing
##@Author: Roger Campbell

##Containers
##Objs ::=  Obj | obj,  Obj1   # one or more terms separated by commas

##Set ::= { } | { Objs }
##['set'] -> {}
##['set', Objs] -> {Objs}
def Set(L):
    return false
##Tup ::= ( Obj , Objs)
##['tup', Obj, Objs] -> (Obj, Objs)
def Tup(L):
    return false

##Seq ::= < > | < Objs> 
## ['seq'] -> < >
## ['seq', Objs] -> <Objs>
def Seq(L):
    return false

##Arithmetic

##exponentiation
##['exp',t1,t2] -> t1^t2
def Exp(L):
    return false

##unary increment
##['inc',t1] -> +t1
def Inc(L):
    return false

##unary decrement
##['dec',t1] -> -t1
def Dec(L):
    return false

##multiplication
##['mul',t1,t2] -> t1 * t2
def Mul(L):
    return false

##division
##['div',t1,t2] -> t1 / t2
def Div(L):
    return false

##addition
##['add',t1,t2] -> t1 + t2
def Add(L):
    return false

##subtraction
##['sub',t1,t2] -> t1 - t2
def Sub(L):
    return false


##Sets

##set product
##['setProd', t1, t2] -> t1 * t2 #t1,t2 are sets
def SetProd(L):
    return false

##sec
##['sec', t1, t2] -> t1 sec t2
def Sec(L):
    return false

##union
##['union', t1, t2] -> t1 U t2
def Union(L):
    return false

##set Diff
##['setDiff', t1, t2] -> t1 / t2
def SetDiff(L):
    return false


##Conditionals

##Less than
##['<', t1, t2] -> t1 < t2
def LT(L):
    return false

##Greater than
##['>', t1, t2] -> t1 > t2
def GT(L):
    return false

##Less than or equal to
##['<=', t1, t2] -> t1 <= t2
def LTE(L):
    return false

##Greater than or equal to
##['>=', t1, t2] -> t1 >= t2
def GTE(L):
    return false

##Equal to
##['=', t1, t2] -> t1 = t2
def EQ(L):
    return false

##Contained in
##['in', t1, t2] -> t1 in t2 #t1 is an Obj t2 is a container
def In(L):
    return false

##subset
##['subSet', t1, t2] -> t1 sub t2 #t1 and t2 are sets
def SubSet(L):
    return false

##Boolean Connectives

##not
##['not', t1] -> ~t1
def Not(L):
    return false

##and
##['and', t1, t2] -> t1 & t2
def And(L):
    return false

##or
##['or', t1, t2] -> t1 V t2
def Or(L):
    return false

##implication
##['imp', t1, t2] -> t1 => t2
def Imp(L):
    return false

##if and only if
##['iff', t1, t2] -> t1 <=> t2
def Iff(L):
    return false
