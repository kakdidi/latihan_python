class Hero:  #template
  def __init__(self, name, health, attackPower, armorNumber):
    self.name = name
    self.health = health
    self.attackPower = attackPower
    self.armorNumber = armorNumber
  
  def serang (self, lawan):
    print(self.name + " menyerang " + lawan.name)
    lawan.diserang(self)
    
  def diserang (self,lawan):
    print(self.name + " diserang " + lawan.name)

sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 5, 10)

sniper.serang(rikimaru)