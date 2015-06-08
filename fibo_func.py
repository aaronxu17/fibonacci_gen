## Fibonacci Number Generation Module @ Aaron Xu##

def fib(pre=0, cur=1):
    yield pre
    while True:
        yield cur
        pre,cur=cur,pre+cur
