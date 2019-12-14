import pygame
import scene
import player


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)

multiplayer = True #это говорит нам, когда у нас включен мультиплеер
player_1 = player.Player(60, 660, 40, 20, "w", "s", "a", "d") #x, y, wight, hight, up, down, left, right
player_characteristic = player_1.make_tuple_of_characteristic()
if multiplayer:
    player_2 = player.Player(120, 720, 40, 20, "up", "down", "left", "right") #x, y, wight, hight, up, down, left, right
    player_characteristic_2 = player_2.make_tuple_of_characteristic()


 #создаём игрока, и главный экран

def actions(keys):
    global player_characteristic
    global player_characteristic_2
    if keys[pygame.K_LEFT]:
        player_1.move_left()

    if keys[pygame.K_RIGHT]:
        player_1.move_right()

    if keys[pygame.K_UP]:
        player_1.move_up()

    if keys[pygame.K_DOWN]:
        player_1.move_down()
    player_characteristic = player_1.make_tuple_of_characteristic()
    

    if multiplayer:

        if keys[pygame.K_a]:
            player_2.move_left()

        if keys[pygame.K_d]:
            player_2.move_right()

        if keys[pygame.K_w]:
            player_2.move_up()

        if keys[pygame.K_s]:
            player_2.move_down()
        player_characteristic_2 = player_2.make_tuple_of_characteristic()

        





run = True
while run:
    pygame.time. delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    actions(keys)
    
    win.fill((0,0,0))#закрашиваем окно
    pygame.draw.rect(win, player_1.color, player_characteristic)
    if multiplayer:
        pygame.draw.rect(win, player_2.color, player_characteristic_2)
    #рисуем игрока

    pygame.display.update()
pygame.quit()