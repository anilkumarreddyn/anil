class Myclass:
	x = 10
	y = 34
	def add(self,a,b):
		print self.x 
		print self.y 
		print self.x,self.y
		return a + b
	@classmethod
	def mul(cls,a,b):
		
		print cls.x,cls.y
		

		return a * b
	@staticmethod
	def div(a,b):
		return a/b

# for instance methods we are creating instance
obj = Myclass()
print obj.add(10,20)

#for class method and static methods no need to create instance directly we can call with class name 
#and static method print Myclass.mul(10,45)
print Myclass.div(76,19)
print Myclass.mul(32,2)
#or else by creating instance we can call the class and static methods
obj2 =Myclass()
print obj2.mul(10,54)

obj3 =Myclass()
print obj3.div(56,14)


