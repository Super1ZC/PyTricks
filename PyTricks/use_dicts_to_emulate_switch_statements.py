def dispatch_if(operator,x,y):
    """This is similar to calculator"""
    if operator == 'add':
        return x+y
    elif operator == 'sub':
        return x-y
    elif operator == 'mul':
        return x*y
    elif operator == 'div':
        return x/y
    else:
        return None
        
def dispatch_dict(operator,x,y):
    """Using anonymous function lambda to display."""
    return{
        'add':lambda: x+y,
        'sub':lambda: x-y,
        'mul':lambda: x*y,
        #dict.get function，return None when the operator 
        #is not key in dict
        'div':lambda: x/y,}.get(operator,lambda:None)()
        
print(dispatch_if('mul',2,8))
print(dispatch_dict('mul',2,8))
print(dispatch_if('unknown',2,8))
print(dispatch_dict('unknown',2,8))
