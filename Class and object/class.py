# Python3 program to demonstrate instantiating a class
'''class Member:
    attr = "Farmer"
    attr2 = 23

# A sample method
    def fun(self):
        print("I'm a", self.attr)
        print("I'm ", self.attr2, "years old")


# Driver code Object instantiation`
Sam = Member()
# Accessing class attributes through objects`
print(Sam.attr)
'''

# Python3 program to demonstrate instantiating a class
'''class Member:
    attr = "Software Developer"
    attr2 = 25

# A sample method
    def fun(self):
        print("I'm a", self.attr)
        print("I'm ", self.attr2, "years old")


# Driver code Object instantiation`
Danny = Member()
# Accessing class attributes through objects`
print(Danny.attr2)
Danny.fun()
'''

# constructor


class Membership:
    def __init__(self, occup, age, name):
        self.occup = occup
        self.age = age
        self.name = name

    def display(self):
        print("Member's occupation: ", self.occup)
        print("Member's name: ", self.name)
        print("Member's age: ", self.age)
        print("===================================================")


mem1 = Membership("S/W Developer", 23, "Sam")
mem1.display()
mem2 = Membership("Electrician", 28, "Danny")
mem2.display()
