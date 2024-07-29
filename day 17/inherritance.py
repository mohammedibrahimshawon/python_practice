# class person:
#     def __init__(self, fname, lname):
#      self.firstname = fname
#      self.lastname = lname

#     def printname(self):
#       print(self.firstname, self.lastname)


# x = person("Ibtesum", "Iqbal")
# x.printname()        
    
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# class Student(Person):
#   pass

x = person("shown", "uddin")
# x = Student("Mike", "Olsen")

x.printname()
