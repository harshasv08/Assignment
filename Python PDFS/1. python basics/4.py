# This function has a variable with
# name same as s.
def f():
# below s is a local variable 
	s = "Hello"
	print(s)

#below s is a Global variable
s = "World"
f()
print(s)
