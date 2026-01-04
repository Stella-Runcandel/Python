#module is a pythonf ile containg code which u want to import into your program
#use import to include a module (built in/ downloaded/ your own)
#usefull to break large programs into reusable seprate files
#print(help("modules"))
#print(help('math'))

import math
print(math.pi)
#or
import math as m
print(m.pi)
#or
from math import e
a, b,c,d = 1,2,3,4
print(e*a)
print(e*b)
print(e*c)
print(e*d)
print(e*e)
a, b,c,d,e = 1,2,3,4,5
print(e*a)
print(e*b)
print(e*c)
print(e*d)
print(e*e)
#we don't use form xyz import abc, cause we could have conflcit of var names