class Vehicles:
   """
   vehicle class to hold info of diff auto vehicles
   """
   def __init__(self, engine, tires):
       self.engine = engine
       self.tires = tires

   def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")
        
   @classmethod
   def bicycle(cls, tires=None): 
       if not tires:
           tires = [cls.default_tire, cls.default_tire] #class-level variable called default_tire
       return cls(None, tires)
# the class itself (Vehicle) is passed into the method as the cls variable, 
# that means when we call cls(), it is equivalent to doing Vehicle() and will invoke the __init__ method. 
# It's beneficial to use the cls variable instead of the class name, 
# because if we ever change the name of the class, then we won't need to modify this function.
"""
__init__ is the only constructor method for the vehciles class. Python doesn't allow creating multiple constructors unlike Java. 
Python will let a single constructor method that we can customize with as done above.
We can work around having to construct a class object with some preset values, we can create convenience methods using what is known
as class method.
A class method is a function attached to the class itself, not an instance of the class, and it has access to any class-level attributes.
To create a class method, we need to use what is known as a decorator.
Decorators are functions or classes that we use to add additional functionality to a function by prefixing the decorator's name with an
at-sgin @ and puttung it on the line above our function or ,method difinitiopn.
"""
  



  
