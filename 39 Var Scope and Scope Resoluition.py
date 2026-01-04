#variable scope -> where a var is visible and acessable
#LEGB ==> local -> enclosed -> global -> built in
#when we call variable we check for local, then enclosed, then global then built in

from math import e
print(e)

#vars dec in function have local scope
def func1():
    a = 1
    print(a)

func1()
#print(a) throws error as a is local var of function, not visisble outside of it
#functions can't see insid eother functions
#we could have

def func2():
    x = -98
    print(x)

def func3():
    x = 6
    print(x)

func2()
func3()

#enclosed ->
def func4():
    x = -98
    def func5():
        #x = 6 if this is not commented then it'd be 6, but with commented it'll sue x -98
        print(x)
    func5()

func4()
#globar vars are declared out of any functions
def func6():
    print(x)
def func7():
    print(x)
x = 3

func7()
func6()
#here e hasn't been declared anywhere but ti's built in, so it'd take it's value
#if theree was a global verion then it'd pick that
#if an elclosed verison existed it'd take that
#if a local verion existed it'd take that
def func16(): 
    print(e)
def func17():
    print(e)

func17()
func16()
