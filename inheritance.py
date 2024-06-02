class Mammal:
    def walk(self):
        print("Walking")


class Dog(Mammal):
    def bark(self):
        print("Barking")


class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.walk()
