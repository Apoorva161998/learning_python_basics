class Parent: 

	def m1(self): 
		print('Parent Class Method called...') 
 
class Child(Parent): 

	def __init__(self): 
		print('Child Class object created...') 

	def m2(self): 
		print('Child Class Method called...') 

obj = Child() 

obj.m1() 

obj.m2() 
