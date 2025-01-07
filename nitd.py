class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute specific to this instance
        self.age = age

    def introduce(self):  # Method using 'self' to access attributes
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Access instance-specific data
p1.introduce()  # Output: My name is Alice and I am 30 years old.
p2.introduce()  # Output: My name is Bob and I am 25 years old.
