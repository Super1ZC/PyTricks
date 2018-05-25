"""It is better to demonstrate it in IDLE"""
a = [1,2,3]
b = a
print(a is b)
print(a == b)
print('*'*10)

c = list(a)
print(a is c)
print(a == c)

#'is' expression evaluates to True if two variables point
#to the same object

#'==' expression evaluates to True if the objects referred to
# by the variables are equal
