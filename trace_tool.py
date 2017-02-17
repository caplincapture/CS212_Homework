from functools import update_wrapper


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1 # indent
        try:
            result=f(*args)
            print '%s<-- %s == %s' % ((trace.level-1)*indent, 
                                      signature, result)
        finally:
            trace.level -= 1 # unindent in the case it throws an error and need to be restored
        return result
    trace.level = 0
    return _f

@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6) 