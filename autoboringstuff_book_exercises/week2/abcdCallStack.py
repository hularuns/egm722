# Calling a() calls b(), then c() and then d(), then after it's completed the a() call,
# it goes onto the next line and does the d() call of a()

def a():
    print('a() starts')
    b()
    print('in between')
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() reutrns')
    
a()
    