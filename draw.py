import pygame



def player(win, player):
    pygame.draw.rect(win, player.color, player.tuple_of_characteristic()) #рисуем игрока

def hit(win, player):
    pygame.draw.rect(win, (0,0,255), player.damage_area, 5)
    
def tarakan(win, tarakan):
    pygame.draw.rect(win, tarakan.color, tarakan.tuple_of_characteristic())

def HP(win, player):
	for i in range (player.health ):
		pygame.draw.rect(win, (255,0 ,0), ((10 + i*30), 10, 10, 10) )

def CD(win, player):
	pygame.draw.rect(win, (255, 0, 0), (700, 10, 100, 20), 3)
	if player.td == 0:
		pygame.draw.rect(win, (255, 0, 0), (700, 10, 100, 20))
	elif player.td < player.cd_max:
		L = 100 - 100*player.td / player.cd_max
		pygame.draw.rect(win, (255, 0, 0), (700, 10, L, 20)) 
