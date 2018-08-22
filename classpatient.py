class Patient:
    def __init__(self, name, age, description):
        self.name=name
        self.age=age
        self.description=description
        
    def __str__(self):
        '''(Patient) -> str
        Output: Returns a string representing of the patient details.
        The format of the string is:
        Name / Age
        Description
        >>> p1 = Patient(‘John’,29,’Patient suffers from dizziness.’)
        >>> print(p1)
        John / 29
        Patient suffers from dizziness.
        '''        
        return "{} / {} \n{}".format(self.name,self.age, self.description)
    
    def add_age(self):
        '''(Patient) -> Patient
        Output: Returns a new Patient object after incrementing the
        age of a patient by 1.
        '''
        # just to help... what is the name, age and description of
        # this patient (the one that you''re inside)? :
        # can i show another idea??ya
        Patient((self, name, age, description)) # <= here we don''t have patient1 var
        # so... what are the attributes?
        #attributes are properties of an obj
        # almost... you don''t have to call __init__, ok?
        # just pass the attributes
        # init is called automatically to initiate the 
        # vars (attributes) of the new created object
        # but how can you just pass the __init__
        
# another way :)

name_of_patient = 'John'
age_of_patient = 29
patient_problem = 'Patient suffers from dizziness.'

# see... we have 3 variables, with different contents...
# now... we''re going to create an object, called Patient
# who waits three attributes: name, age and description, right?

#so...
patient_object = Patient(name_of_patient, age_of_patient, patient_problem)
# in the __init__ method we have:
# (self, name, age, description)
# self is the object, required to all methods of the object
# name will receive the contents of name_of_patient var
# age will receive the contents of age_of_patient and
# description will receive the contents of patient_problem so far
#... these variables will receive the contents...
# but the object variable ALWAYS begin with self, ok?
# so... self.name receives name... self.age receives age...
# and self.description receives description.

# if you want to access any of these attributes... use like this

patient_object.name
patient_object.age
patient_object.description

#see... any object attributes can be accessed using the name
#of the var, a dot, and the name of the attribute
# INTERNALLY, inside the class... it''s not known the name
# of the variable... so.. you have to use
# a class isn't an object.
# to create an object, you have to instanciate a class... like this

patient1 = Patient('John', 29, 'Patient suffers from dizziness.')
# what happened in the last line? 
# then you call the class Patient... it 'passes' the attributes
# to instantiate a new object.
# initiating ==> self.name, self.age and self.description
# remember... self is the object itself
# so... self.ANYTHING always calls the attributes or the methods
# inside the object...

# the last line has created an object, whose contents is now
# refered by patient1 variable, ok?

# so, to create an object, just call the class name, with
# its attributes, in the case, name, age and description
# right? :) so I should call class in the class? SURE :)