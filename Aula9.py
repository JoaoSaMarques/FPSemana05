class Item:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.canDrop = True
        self.canSell = True
        self.canEquip = True
        
    def log(self):
        print(f"Item: {self.name}, Value: {self.value}, Can Drop: {self.canDrop}, Can Sell: {self.canSell}, Can Equip: {self.canEquip}")
        
class Sword(Item):
    def __init__(self, name, value, damage):
        super().__init__(value, name)  
        self.damage = damage
        
    def log(self):
        super().log()  
        print(f"Damage: {self.damage}")  
        
class Vorpal(Sword):
    def __init__(self, name, value, damage, crit):
        super().__init__(name, value, damage)
        self.criticalrate = crit
        
    def log(self):
        super().log() 
        print(f"Critical Rate: {self.criticalrate}")  
        
# Creating instances and logging their details
potion = Item(5, "Potion")
potion.log()

sword1 = Sword("Sword", 50, 10)
sword1.log()

vorpal = Vorpal("Claymore", 500, 10, 1)
vorpal.log()  