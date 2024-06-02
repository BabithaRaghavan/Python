class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def get_name(self):
		print("Your Name is "+ self.name)

	def get_age(self):
		print("Your Age is "+self.age)


person1 = Person("Linesh","45")
person1.get_name()
person1.get_age()

person2 = Person("Babitha","38")
person2.get_name()
person2.get_age()