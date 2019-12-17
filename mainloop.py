
import player_config  
import pygame
import scene


import tarakan
import draw
import os


action_left_pictures = [pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro1')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro2')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro3')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro4')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro5')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro6')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro7')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro8')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','pro9')),
]

action_up_pictures = [pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor1')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor2')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor3')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor4')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor5')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor6')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor7')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor8')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','professor9')),
]

action_right_pictures = [pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p1')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p2')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p3')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p4')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p5')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p6')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p7')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p8')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','p9')),
]

action_down_pictures = [pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por1')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por2')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por3')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por4')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por5')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por6')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por7')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por8')),
pygame.image.load(os.path.join('/home/sergey/levin-927_game/','por9')),
]


def actions(keys, player):
    if keys[pygame.K_a]:
        print("helo")
        player.actions_pictures = action_left_pictures[player.movie_count%9]
        
        player.move_left()
        
        

    if keys[pygame.K_d]:
        
        player.actions_pictures = action_right_pictures[player.movie_count%9]
        player.move_right()
        

    if keys[pygame.K_w]:
        
        player.actions_pictures = action_up_pictures[player.movie_count%9]
        player.move_up()
        

    if keys[pygame.K_s]:
        
        player.actions_pictures = action_down_pictures[player.movie_count%9]
        player.move_down()
        

    if keys[pygame.K_UP]:
        
        player.actions_pictures = action_up_pictures[2]
        player.damage_up()

    if keys[pygame.K_DOWN]:
        player.actions_pictures = action_down_pictures[0]
        player.damage_down()

    if keys[pygame.K_LEFT]:
        player.actions_pictures = action_left_pictures[5]
        player.damage_left()

    if keys[pygame.K_RIGHT]:
        player.actions_pictures = action_right_pictures[1]
        player.damage_right()

    
    if keys[pygame.K_SPACE]:
        player.change_weapon()


'''
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

'''


def lets_play(run):
    win = pygame.display.set_mode((1000,1000))
    player = player_config.Player(500, 500, 40, 20) #x, y, half_wight, half_hight
    for i in range (0, 5):
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
                if tar.type == 0:
                    tar.picture_move = pygame.image.load(os.path.join('/home/sergey/levin-927_game/','tarakan_left.png'))
                else: 
                    tar.picture_move = pygame.image.load(os.path.join('/home/sergey/levin-927_game/','clop'))
                draw.tarakan(win, tar, player)
                tar.dinamics(player)
                player.get_damage(tar)
                if tar.health <= 0:
                    room.tarakanS.remove(tar)
    

            if room.time_before_create > 0:
                room.time_before_create -= 1
            if len(room.tarakanS) == 0:
                if room.number_wave > room.list_enemies[0]:
                    draw.gate(win, room.gate.coordinates)
                    room.output(player)
                else:
                    draw.pip(win)
                    if ( abs( player.x - 500 ) < 25 ) and ( abs( player.y - 500 ) < 25 ):
                        room.create_enemies(scene.list_enemies)



            pygame.display.update()

        if room.gate.victory == 0:
            break 
            '''
    pygame.quit()
    if player.health == 0:
        title_death
    else: title_victory(run) '''






#menu()
run = True
lets_play(run)
pygame.quit()