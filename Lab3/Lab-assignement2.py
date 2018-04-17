#### Main class
class Baby(object):
    ''' Class created for Lab 2 exercise, for testing single use object cretion from this class'''
    __instance = None                               # Variable __instance is set to "None"

    def __new__(cls, name):                         # Override of __new__ function to instantiate the class
        if Baby.__instance is None:                 # Check the __instance variable, if somebody has already instantiated this class
            Baby.__instance = object.__new__(cls)   # If previous is not true, class object is instantiated
            Baby.__instance.name = name             # During the instantiation set the attribute name
            print('Baby is initialized and name set to : {}'.format(Baby.__instance.name))
        else:
            raise TypeError('Too many Babys created') # If class is already instantiated, raise error and exit
        return Baby.__instance                      # end of function __new__ and return the attributes


#### End of class


#### Work area
# First try
baby1 = Baby('Juhan')
print(baby1.name)
print(type(baby1))

# Second try
baby2 = Baby('Pets')
#print(baby2.name)
#print(type(baby2))






