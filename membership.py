x = 'Geeks for Geeks'
y = {3:'a',4:'b'}
print('G' in x)
 
print('geeks' not in x)
 
print('Geeks' not in x)
 
print(3 in y)
 
print(4 in y)
print ('a' in y)

a = 2
b = 3
sum = a + b
print(sum)
print '===' *6

a1 = 3
b1 = 3
print id(a1)
print id(b1)
print "--"* 6
print id(a1==b1)
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3]
b3 = [1,2,3]	

print (a1 is  b1)
	
	
print(a2 is b2)
	
# Output is False, since lists are mutable.
print(a3 is b3)

print '##' *6
a = True
b = False
 
# Print a and b is False
print(a and b)
 
# Print a or b is True
print(a or b)
 
# Print not a is False
print(not a)

print '%%' *6

a = 10
b = 4
 
# Print bitwise AND operation  
print(a & b)
 
# Print bitwise OR operation
print(a | b)
 
# Print bitwise NOT operation 
print(~a)
 
# print bitwise XOR operation 
print(a ^ b)
 
# print bitwise right shift operation 
print(a >> 2)
 
# print bitwise left shift operation 
print(a << 2)


a = 'Geeks'
print a # output is displayed
print id(a)
a = a + 'for'
print a # works fine
print id(a)

print '^^' *6
a = 'Geeks' # string with single quotes
b = "for"   # string with double quotes
c = '''Geeks
a portal
for
geeks'''    # string with triple quotes
print a
print b
print c
 
# Concatenation of strings created using
# different quotes
print a + b 
print a + b +c


print "Hi Mr Geek."
 
# use of escape sequence
print 'He said , "Welcome to Geeks for Geeks" '
 
print 'Hey so happy to be here'
 
# use of mix quotes
print 'Getting Geeky, "Loving it" '            


print "He said, \"Welcome to GeeksforGeeks\""
print 'He said, \" hiii Welcome to GeeksforGeeks\"'


a = 'anil'
print len(a)

b ='ganesh'
print len(b)


a =[1,2,3,4,56,78]

print a[3]
print a[5]

str ='techno guru'
print str[:-1]
print str[-4:-1]
#print str[-4:-1:-2]
print str[-1:]
print '**' *6
print str[-1::-1]
print str[-2:-5:-2]

x = "Welcome to GeeksforGeeks"
 
# Prints substring from 2nd to 5th character
print x[2:5]      
 
# Prints substring stepping up 2nd character 
# from 4th to 10th character
print x[4:10:2]    
 
# Prints 3rd character from rear from 3 to 5
print x[-5:-3]
print x[-5:-3:1] 
print x[-1::-2]

print x[::-1]
print x[::1]

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)