class Dog :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")
    


my_dog = Dog("Buddy", 3)

i= int(2)

my_dog.get_info()
Dog.get_info(my_dog)



my_dog.bark()