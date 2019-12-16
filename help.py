import pygame
import scene
import player
import tarakan
import draw


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player_1 = player.Player(60, 660, 40, 20) #x, y, half_wight, half_hight
scene_1.scene_object_for_drawing = []
scene_1.scene_object_for_drawing.append(player_1)

tarakanS = [] #Множество всех тараканов
scene_1.scene_object_for_drawing.append(tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5))
scene_1.scene_object_for_drawing.append(tarakan.Tarakan(300, 600, 40, 20, 50, 1))



 #создаём игрока, и главный экран

def actions(keys):
    if keys[pygame.K_a]:
        player_1.move_left()

    if keys[pygame.K_d]:
        player_1.move_right()

    if keys[pygame.K_w]:
        player_1.move_up()

    if keys[pygame.K_s]:
        player_1.move_down()

    if keys[pygame.K_UP]:
        player_1.damage_up()

    if keys[pygame.K_DOWN]:
        player_1.damage_down()

    if keys[pygame.K_LEFT]:
        player_1.damage_left()

    if keys[pygame.K_RIGHT]:
        player_1.damage_right()

    
    if keys[pygame.K_SPACE]:
        player_1.change_weapon()


def all_drawing():
    
    for objects in scene_1.scene_object_for_drawing:
        if type(objects) is player.Player:
            draw.draw_player(win,objects)
        if type(objects) is tarakan.Tarakan:
            if objects.health >= 0:
                draw.tarakan(win, objects)
                objects.dinamics(player_1)
                player_1.get_damage(objects)

        

        






'''for i in range 4:
    scene.room(i)'''
run = True
while (player_1.health > 0) and run:
        pygame.time. delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = Falsed
        keys = pygame.key.get_pressed()
        actions(keys)

        player_1.damage()
    
        draw.room(win)#рисуем локацию
        all_drawing()


        pygame.display.update()
pygame.quit()


class Scene():
    def __init__(self):
        self.size = (1000,1000)
        self.scene_object_for_drawing = []
    
    
    def make_it_for_drawing(self, object):
        self.scene_object_for_drawing.append(object)
    

