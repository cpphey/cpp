import numpy as np

#l = np.array([1,2,3])
#print(l.size())


def forloop():
    l = [ 'a','b','c']
    for i in range(0,3,1):
        print(i, "=", l[i])
    else:
        print("afterloop")

forloop()

class Hey:
    arg = 'memberData'
    def __init__ (self,arg='default'):
        self.arg=arg
        print('assigned in Hey class '+arg)

h = Hey()
h1 = Hey('from outside')

def foo1():
    x=5 #variable assignment

    #import sys
    #sys.exit(10) #exit code
    #sys.exit(-10) #is 256 - 10 = 246 TRICK

    x=10
    x+5
    x-2
    x*2
    div = x/2 # div is float ; x is int and 2 is an INT also
    #Contrast below with top
    div = x / 2.1 # div is float ; x is int and 2 is an INT also

    #TYPE and TYPE CASTING
    op = bool("True") #Works
    op = int(1.1) #works
    op = int("1.1") #does not work ; ValueError: invalid literal for int() with base 10: '1.1'
    op = float("1.1")
    type("1.1") # <class 'str'>

"""
String
type('str')
<class 'str'>
type("str")
<class 'str'>
testStr="Hey"
testStr*2
'HeyHey'
testStr+2
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
testStr+"2"
'Hey2'
testStr+"2"+"3"
'Hey23'
"y" in testStr
True
'y' in testStr
True
"""

"""
Multi line comment
# - Hash is a single line comment
"""


def sing(a = "defaultarg"):
    print(a)

sing()
sing("otherArg")
d={'a':'dictArg'}
d=dict(a='dictArg')
sing(**d)

def multipleR(a='default'):
    return (1, 2)

ret = multipleR()
print("done")

