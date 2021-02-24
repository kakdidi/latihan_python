class Hero:  #template
	def __init__(self, inputName, inputHealth, inputPower, inputArmor):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 4)
print(hero1.__dict__)
