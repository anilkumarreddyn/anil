a ={'a':1,'b':2}
print a.keys() 
print a.values()
print a.items()
#updation with new value
a['b'] = 'anil' 
print a
#insert a new key  and values we will get item
a['c'] = 3
print a

del a['b']
print a

a['b'] = 2
print a
print a.viewkeys()
print a.viewvalues()
print a.viewitems()
print a.iterkeys()
print a.itervalues()
print a.iteritems()
a.pop('b')
print a

'''a['ashok'] = 'name'
print a'''
a['b'] =2
print a
a['d'] =4
print a

#first insertion will be removed first
a.popitem()
print a
a.popitem()
print a
a.popitem()
print a


#ex:
a ={'a':1,'b':2}
print a.get('b')
print a.get('a')
print a.get('x')
print a.get('c',['abc','def'])
print a.get('name','ashok')
print a.get('c')

#setdefault
a.setdefault('c')
print a
a.setdefault('d',12)
print a
#clear all the items
b = {'x':1,'y':2,'z':3}
b.clear()
print b
#b.clear('x')



print a
a.pop('c')
print a

print a.fromkeys((1,'a'),'Hello')
print a.fromkeys((1,2,3),'hiii')
print a.fromkeys('123','anil')
#print a

print a.fromkeys('abc','anil')
print a.fromkeys(['abc'],'ashok')

print a.fromkeys(['123'],'ashok')
print a.fromkeys('1','hiii')
print a.fromkeys((1,'anil'),'abhi')
print a.fromkeys(('xyz','akshar'),'hi')
print a.fromkeys((0,1),'cherry')
print a.fromkeys((0,1))











