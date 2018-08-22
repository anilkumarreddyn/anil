class student:
	name ='anil'
	rno = 123
	address ="bangalore"
	def __init__(self,a,b):
		self.a =a 
		self.b =b
		print self.a,self.b
	def add(self,x,y):
		return x+y
obj =student(10,20)
print obj.name
print obj.rno
print id(obj.rno)
print obj.address
print obj.add(34,6)

obj.name ='ashok'
print obj.name

obj.school ='narayana'
print obj.school

print obj.name
print obj.rno

obj.rno =12222
print obj.rno

print obj.name
print obj.rno
print obj.address

obj.address ='chennai'
print obj.address


print obj.name
print obj.rno
print obj.address

print id(obj.rno)



obj2 = student(122,344)
print obj2.rno
print obj2.name
print obj2.address

print id(obj2.rno)
print id(obj.rno)
