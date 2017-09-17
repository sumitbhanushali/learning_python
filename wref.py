#weakref.finalize() executes callback function when object is destroyed
import weakref
s1 = {1,2,3}
s2 = s1

def bye():
    print('object destroyed')

ender = weakref.finalize(s1,bye)
s2 = 'ss' #this destroys object
