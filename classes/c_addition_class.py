class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name,  "I am ",  self.age, "years old")

p1 = Person("Peter", 32)
p1.myfunc()

