class Demo(object):
    def __init__(self, value):
        self.value=value
        if value==2:
            raise ValueError
    def __del__(self):
        print ('__del__', self.value)


d=Demo(2)  
