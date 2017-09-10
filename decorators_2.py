import time

#in this decorator problem is that name of decorated function is changed and does not accept kwargs
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r'%(elapsed,name,arg_str,result))
        return result
    return clocked

@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

#equivalent of decorator
factorial = clock(factorial)

print(factorial(6))

import functools

#improvised version
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs):
        elapsed = time.time() - t0
        name = func._name_
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked