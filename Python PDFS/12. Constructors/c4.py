class Person:
    def __init__(self, name, age):
        # Constructor with attributes
        self.name = name  
        self.age = age    
if __name__ == "__main__":
    #  objects of the Person class with attributes
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    #attributes of the objects
    print(f"{person1.name} is {person1.age} years old.")
    print(f"{person2.name} is {person2.age} years old.")
