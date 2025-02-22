import pygame
import player_config

def draw_player(win,object):
	player(win, object)
	HP(win, object)
	damage(win, object)
	CD(win, object)

def player(win, object):
    win.blit(object.actions_pictures,(object.x, object.y - object.half_hight))#рисуем игрока
    
def tarakan(win, tarakan, player):
	
	win.blit(tarakan.direction(player),(tarakan.x - tarakan.half_wight, tarakan.y- tarakan.half_hight ))

def HP(win, player):
	for i in range (player.health ):
		pygame.draw.rect(win, (255,0 ,0), ((10 + i*30), 10, 10, 10) )

def CD(win, player):
	pygame.draw.rect(win, (255, 0, 0), (800, 10, 100, 20), 3)
	if player.td == 0:
		pygame.draw.rect(win, (255, 0, 0), (800, 10, 100, 20))
	elif player.td < player.cd_max:
		L = 100 - 100*player.td / player.cd_max
		pygame.draw.rect(win, (255, 0, 0), (800, 10, L, 20)) 

def damage(win, player):
	if player.td > player.cd_max*player.weapon:
		if player.weapon == 1:
			lazer(win, player)
		else:
			bullet(win, player)

def lazer(win, player):
    win.blit(player.lazer.picture, player.lazer.coordinates)

def bullet(win, player):
	for bullet in player.bullets:
		win.blit(bullet.picture,bullet.coordinates)

def room(win):
	win.fill((0,0,0))

def gate(win, coordinates):
	pygame.draw.rect(win, (255, 255 ,255), coordinates )


def start_page(win):
	win.fill((255, 215, 0))

def title_victory(win):
	win.fill((255, 255, 255))

def title_death(win):
	win.fill((128, 0, 0))

def pip(win):
	pygame.draw.rect(win, (255, 0, 0), (475, 475, 50, 50), 5)