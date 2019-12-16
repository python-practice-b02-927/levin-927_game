import pygame
import scene
import player
import tarakan
import draw


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player = player.Player(60, 660, 40, 20) #x, y, half_wight, half_hight


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


 





for i in range (0, 4):
    room = scene.Room(i)
    run = True
    while (player.health > 0) and (room.gate.victory == 0) and run:
        pygame.time. delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        actions(pygame.key.get_pressed())

        room.create_enemies(scene.list_enemies)
        player.damage()
    

        draw.room(win)#рисуем локацию
        draw.draw_player(win, player)


        for tar in room.tarakanS:
            draw.tarakan(win, tar)
            tar.dinamics(player)
            player.get_damage(tar)
            if tar.health <= 0:
                room.tarakanS.remove(tar)
    

        if len(room.tarakanS) == 0:
            draw.gate(win, room.gate.coordinates)
            room.output(player)


        pygame.display.update()

    if room.gate.victory == 0:
        break

pygame.quit()