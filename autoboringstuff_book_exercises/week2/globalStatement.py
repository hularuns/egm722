def spam():

    global eggs 
    eggs = 'spam'

eggs='global'
#because i've now called spam(), it replaces the global eggs just above.
spam()
print(eggs) #will print spam, if i put eggs='global' below spam(), it'll print (global)
