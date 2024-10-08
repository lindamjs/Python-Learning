class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

class GoldenRetriever(Dog):
    def fetch(self):
        print("Fetching the ball")

dog1 = Dog("Buddy", "Golden Retreiver")
dog2 = Dog("Max", "Labrador")
dog3 = GoldenRetriever("Charlie", "Golden Retriever")

print(dog1.name, dog1.breed)
dog1.bark()

print(dog3.name, dog3.breed)
dog3.bark()
dog3.fetch()

#############################################################

dog4 = Dog("Buddy", "Golden Retreiver")
dog4.set_name("Tyson")
print("Setting the name :", dog4.get_name())