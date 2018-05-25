test = {True:'yes',1:'no',1.0:'maybe'}

print(test)

#The output is {True:'maybe'}
#This answer is amazing and it is based on the situation:
# True == 1 == 1.0 !!!!!important

#The progress happens like
#1: test = dict()
#2: test[True] = 'yes'
#3: test[1] = 'no'
#4： test[1.0] = 'maybe'
#Due to the fact that 'True == 1 == 1.0',it is equal to 
#3: test[True] = 'no'
#4: test[True] ='maybe'

#As a resultl, you can also get this ['yes','no','maybe'][True]
#The output is 'no'

#This happens because the boolean type is a subtype of the ingeter type
#and bollean values behave like the values 0 and 1.

#The key is still True because Python's dictionaries don't update the
#key object itself when a new value is associated with it.
#ys = {1.0:'no'}
#ys[True] = 'yes'
#print(ys) ----->   {1.0:'yes'}

"""The Python dictionary uses hash table to store the key,value pair.
    The hash value is derived from the key as a numeric value of a
    fixed length that uniquely identifies the key.
    
    There are a few more tests here"""
class SameHash:
    def __hash__(self):
        return 1
        
a = SameHash()
b = SameHash()
print(a == b)

print(hash(a),'   the hash value of a')
print(hash(b),'   the hash value of b')

test2 = {a:'a',b:'b'}
print(test2)

#Summary: This condition is necessary:
#key1 == key2 ==key3
#To have the overwritten situation in dict's value assignment
    
