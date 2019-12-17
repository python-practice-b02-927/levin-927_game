import draw
from tarakan import Tarakan as T

#   [ type, wight, hight,  HP,  speed,       color,     jump_duration,  jump_cd, jump_speed]
S  = (  0,     40,    40,   50,     2,    (   0, 255, 0),       40,          100,       10)
M  = (  1,     60,    60,  100,     3,    ( 255, 165, 0),        0,          500,       0 )
L  = (  2,     80,    80,  200,     4,    ( 255,  69, 0),        0,          100,       0 )
XL = (  3,    120,   120,  500,     3,    ( 139,   0, 0),       40,          500,       4 )
BOSS=(  4,    500,   500, 3000,     2,    ( 139,  69,19),       0,             0,       0 )

list_enemies = []
#начальная комната
list_enemies.append([])
#первая комната
list_enemies.append([
T(150, 500, M),
T(411, 300, M),
T(712, 110, L),
T( 31, 814, L)
])
#вторая комната
list_enemies.append([
T(150, 850, L),
T(850, 850, L),
T(850, 150, L),
T(150, 150, XL)
])
#третья комната
list_enemies.append([
T(150, 150, S),
T(400, 373, S),
T(105, 911, S),
T(300, 600, M)
])
#Босс - комната
list_enemies.append([
T(750, 500, BOSS)
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
		if ( player.x + player.half_wight >= 960 ) and ( player.y + player.half_hight - self.size < 500 ) and ( player.y - player.half_hight + self.size > 500 ):
			self.victory = 1
			player.x = player.half_wight + 10





