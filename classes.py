class A:
	x = 10
	y = 23
	z = 67
	

obj =A()




obj.x = 20
obj.y =34
obj.z =767

print obj.x 
print obj.y

print id(obj.x)


obj1 =A()
print obj.x
print id(obj1.x)