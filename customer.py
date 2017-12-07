# Valentina Vogel
# 16-708-919

from vehicle import *
import random


class Customer(object):
    
    def __init__(self,name):
        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):
        return "Customer: {}".format(self.__name)

    def credit_score(self):
        number = random.randint(1,100)
        if number > 60:
            return True
        else:
            return False

    def get_score(self):
        return self.__score


class VIP_Customer(Customer):

    def credit_score(self):
        return True


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

#print(Wendy) # expected output: Customer: Wendy
#print(Heidi) # expected output: Customer: Heidi

#print(Wendy.get_score()) # expected output: True
#print(Heidi.get_score()) # expected output: True
