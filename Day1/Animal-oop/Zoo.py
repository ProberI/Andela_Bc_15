from Animal_server import Animal
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self
		

Dog1 = Dog('clifford')

Dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print 'This is a Dragon!'
		super(Dragon, self).displayHealth()
		return self

Dragon1 = Dragon('Puff')

Dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()