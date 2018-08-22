class Company:
	l=['anil','ashok']
	name ='cgi'
	rno  = 133
	domain ='python'
	salary = 275000
	
	def work(self,l):
		print True
		print self
		return l
	def work1(self,a,b):
		print False
		print self
		return a+b

details = Company()
print details

print details.name
print details.rno
print details.domain
print details.l
print details.salary
print details.work(10)
print details.work1('ashok','anil')

def add(x,y =10,z=20):
	return x+y+z

print add(10)
print add(10,20)
print add(20,30,80)
print '====' * 6
def printAndReturnNothing():
    x = "hello"
    print(x)

def printAndReturn():
    x = "hello"
    print(x)
    return x

def main():
    ret = printAndReturn()
    other = printAndReturnNothing()

    print("ret is: %s" % ret)
    print("other is: %s" % other)

if __name__ == "__main__":
    main()



def add(ele,l=[]):
	l.append(ele)
	return l
print add(10)
print add(20)
print add(30)
print add(40,[20])




