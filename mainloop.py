import pygame
import scene
import player
import tarakan


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player = player.Player(60, 660, 40, 20) #x, y, wight, hight




tarakanS = [] #Множество всех тараканов
tarakanS.append(tarakan.Tarakan(60 , 600, 40, 20, 100, 0.5))
tarakanS.append(tarakan.Tarakan(300, 600, 40, 20, 50, 1))



 #создаём игрока, и главный экран

def actions(keys):
    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_d]:
        player.move_right()

    if keys[pygame.K_w]:
        player.move_up()

    if keys[pygame.K_s]:
        player.move_down()

    if keys[pygame.K_LEFT]:
        player.hit_left()

    if keys[pygame.K_RIGHT]:
        player.hit_right()

    if keys[pygame.K_UP]:
        player.hit_up()

    if keys[pygame.K_DOWN]:
        player.hit_down()  
 










run = True
while run:
    pygame.time. delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    actions(keys)
    
    win.fill((0,0,0))#закрашиваем окно
    pygame.draw.rect(win, player.color, player.tuple_of_characteristic())   #рисуем игрока

    for tar in tarakanS:
        if tar.health >= 0:
            pygame.draw.rect(win, tar.color, tar.tuple_of_characteristic())
            tar.dinamics(player)
            player.get_damage(tar)


    if player.cd != 0:
        player.damage()
        pygame.draw.rect(win, (0,0,255), player.damage_area, 5)





    pygame.display.update()
pygame.quit()