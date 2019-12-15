import pygame
import scene
import player
import tarakan


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player = player.Player(60, 660, 40, 20) #x, y, wight, hight
player_characteristic = player.make_tuple_of_characteristic()

tarakan = tarakan.Tarakan(60, 500, 40, 20) #x, y, wight, hight
tarakan_characteristic = tarakan.make_tuple_of_characteristic()



 #создаём игрока, и главный экран

def actions(keys):
    global player_characteristic
    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_d]:
        player.move_right()

    if keys[pygame.K_w]:
        player.move_up()

    if keys[pygame.K_s]:
        player.move_down()
    player_characteristic = player.make_tuple_of_characteristic()
    


        





run = True
while run:
    pygame.time. delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    actions(keys)
    
    win.fill((0,0,0))#закрашиваем окно
    pygame.draw.rect(win, player.color, player_characteristic)   #рисуем игрока
    pygame.draw.rect(win, tarakan.color, tarakan_characteristic)


    pygame.display.update()
pygame.quit()