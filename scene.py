import tarakan
import draw

list_enemies = []
#начальная комната
list_enemies.append([])
#первая комната
list_enemies.append([
tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5, (0, 255, 0) ),
tarakan.Tarakan(300, 600, 40, 20, 50 ,   1, (0, 255, 0) )
])
#вторая комната
list_enemies.append([
tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5, (255, 215, 0) )
])
#третья комната
list_enemies.append([

])
#Босс - комната
list_enemies.append([

])




class Room():
	def __init__ (self, i):
		self.number = i
		self.gate = Gate()
		self.time_before_create_max = 50
		self.time_before_create = 2*self.time_before_create_max
		self.tarakanS = []

	def create_enemies(self, list_enemies):
		if self.time_before_create == 0:
			self.tarakanS = list_enemies[self.number]
		else:
			self.time_before_create -= 1 

	def output(self, player):
		if self.time_before_create == 0:
			self.gate.input(player)

class Gate():
	def __init__ (self):
		self.size = 100 
		self.wight = 10
		self.coordinates = (0, 500-self.size, 2*self.wight, 2*self.size)
		self.victory = 0

	def input(self, player):
		self.coordinates = (990-self.wight, 500-self.size, 2*self.wight, 2*self.size )
		if ( player.x + player.half_wight >= 990 ) and ( player.y + player.half_hight - self.size < 500 ) and ( player.y - player.half_hight + self.size > 500 ):
			self.victory = 1
			player.x = player.half_wight + 10




class Scene():
    def __init__(self):
        self.size = (1000,1000)


