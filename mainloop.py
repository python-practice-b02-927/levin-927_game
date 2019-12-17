import pygame
import scene
import player_config  
import tarakan
import draw


def actions(keys, player):
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

    
    if keys[pygame.K_q]:
        player.change_weapon()




def menu():
    win = pygame.display.set_mode((1000,1000))
    run = True
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw.start_page(win)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.quit()
            lets_play(run)
            win = pygame.display.set_mode((1000,1000))
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False
        pygame.display.update()


def title_victory(run):
    win = pygame.display.set_mode((1000,1000))
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False        
        draw.title_victory(win)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            break
        pygame.display.update()
    pygame.quit()

def title_death(run):
    win = pygame.display.set_mode((1000,1000))
    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False        
        draw.title_death(win)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            break
    pygame.quit()


def lets_play(run):
    win = pygame.display.set_mode((1000,1000))
    player = player_config.Player(500, 500, 40, 20) #x, y, half_wight, half_hight
    for i in range (0, 4):
        room = scene.Room(i)
        while (player.health > 0) and (room.gate.victory == 0) and run:
            pygame.time. delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            actions(pygame.key.get_pressed(), player)

            room.create_enemies(scene.list_enemies)
            player.damage()
    

            draw.room(win)                  #рисуем локацию
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
    if player.health == 0:
        title_death
    else: title_victory(run)






menu()
pygame.quit()