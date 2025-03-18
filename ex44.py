# Inheritance
class Parent:
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#Composition

class Other:
    def override(self):
        print("OTHER override()")

class Child:
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.override()

son = Child()
son.implicit()
