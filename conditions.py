def main():
	x,y =8,4
	
	if(x < y):
		st= "x is less than y"
	else:
		st= "x is greater than y"
	print (st)
	
if __name__ == "__main__":
	main()


def main():
    x,y =8,4
    
    if(x < y):
        st= "x is less than y"
        print (st)
    

print main()

print'==' *5

def main():
	x,y =8,8
	
	if(x < y):
		st= "x is less than y"
	
	elif (x == y):
		st= "x is same as y"
		return st
		

	
	else:
		st="x is greater than y"
	print(st)
	

print main()

def main():
	x,y = 10,8
	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print(st)
	
if __name__ == "__main__":
	main()


print '**'*7


total = 100
country = "US"
#country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
        print("Shipping Cost is $25")
elif total <= 150:
	    print("Shipping Costs $5")
else:
        print("FREE")
if country == "AU": 
	  if total <= 50:
	    print("Shipping Cost is  $100")
else:
	    print("FREE")


def main():
  print "Hello!"
  return True
  
if __name__== "__main__":
	print   main()

print "Guru99"


# Declare a variable and initialize it
f = 101
print f
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print f
someFunction()
print f


print '^^' * 6

f = 101;
print f
# Global vs.local variables in functions
def someFunction():
  global f
print f
f = "changing global variable"
someFunction()
print f 



def greet(name):
	print ("Hello, " + name + ". Good morning!")
	return name

print greet('anil')


def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))


