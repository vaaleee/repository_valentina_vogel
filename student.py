from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module): # changed it to module!
        self.modules.append(module)
        self.grades[module.get_title()] = module.get_grade()

    def get_list_modules(self):
        print("Modules of Student {}:".format(self.name))
        for item in self.modules:
            print(item)

    def get_grades(self):
        print("Grades of Student {}:".format(self.name))
        for item in self.grades:
            print("{}: {}".format(item, self.grades[item]))


### test cases ###

me = Student("Valentina Vogel")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6


