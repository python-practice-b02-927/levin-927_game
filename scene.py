import tarakan

list_enemies = []
list_enemies.append([
#начальная комната
tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5, (0, 255, 0) ),
tarakan.Tarakan(300, 600, 40, 20, 50 ,   1, (0, 255, 0) )
])
#первая комната
list_enemies.append([
tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5, (255, 215, 0) )
])
#вторая комната
list_enemies.append([0

])
#третья комната
list_enemies.append([0

])
#Босс - комната
list_enemies.append([0

])


class Room():
	def __init__ (self, i):
		self.victory = 0
		self.number = i

	def create_enemies(self, list_enemies):
		print(list_enemies[self.number])
		self.tarakanS = list_enemies[self.number]

	def end(self):
		if len(self.tarakanS) == 0:
			self.victory = 1




class Scene():
    def __init__(self):
        self.size = (1000,1000)


