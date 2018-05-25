def func1(a,b):
    return a+b

def func2(a,b):
    return a*b

#This step is the core! Putting functions into a list for
#further operation
funcs = [func1,func2]

#There is no need to use print function in IDLE to 
#see the results.
print(funcs[0])
print(funcs[1])

print(funcs[0](2,3))
print(funcs[1](2,3))
