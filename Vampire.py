class Vampire(object):
	def __init__(self):
		self.health = 6
		self.power = 2
		self.name = "Vampire"
		self.xp_value = 10

	def take_damage(self,damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0