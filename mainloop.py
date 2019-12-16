import pygame
import scene
import player
import tarakan
import draw


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player = player.Player(60, 660, 40, 20) #x, y, half_wight, half_hight




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

    if keys[pygame.K_UP]:
        player.damage_up()

    if keys[pygame.K_DOWN]:
        player.damage_down()

    if keys[pygame.K_LEFT]:
        player.damage_left()

    if keys[pygame.K_RIGHT]:
        player.damage_right()

    if keys[pygame.K_SPACE]:
        player.change_weapon()


 







run = True
while (player.health > 0) and run:
    pygame.time. delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    actions(keys)

    player.damage()
    
    win.fill((0,0,0))#закрашиваем окно
    draw.player(win, player)

    draw.HP(win, player)

    for tar in tarakanS:
        if tar.health >= 0:
            draw.tarakan(win, tar)
            tar.dinamics(player)
            player.get_damage(tar)



    draw.damage(win, player)
    

    draw.CD(win, player)

    





    pygame.display.update()
pygame.quit()