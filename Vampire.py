class Vampire(object):
	def __init__(self):
		self.health = 6
		self.power = 2
		self.name = "Vampire"

	def take_damge(self,damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0