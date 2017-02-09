
class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print 'Name:' + self.name + '\nHealth:' + str(self.health) + '\n'
		return self


Animal1 = Animal('Goat')

Animal1.walk().walk().walk().run().run().displayHealth()
