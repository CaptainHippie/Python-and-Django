def fib(n):
    a,b= 0,1
    while a<n:
        print(a, end=', ')
        a,b=b,a+b
    print()
    
s = "If comrade Napolean says it, he must be right"

def foo(arg):
    print(f'arg= {arg}')
    
class Foo:
    pass 