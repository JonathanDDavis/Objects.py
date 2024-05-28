#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     26/09/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##class score:
##  x=0
##playerScore = score()
##print(playerScore.x)

class person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def personGreeting(self):
        print("Hello, I am " + self.name)

##player = Person("John", 0)
##
##print("What is your name?")
person.name = input()
##
##player.personGreeting()


print(person.name)
##print(player.age)
