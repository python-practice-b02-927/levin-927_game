import pygame
import scene
import player
import tarakan


scene_1 = scene.Scene()

win = pygame.display.set_mode(scene_1.size)


player = player.Player(60, 660, 40, 20) #x, y, wight, hight
player_characteristic = player.make_tuple_of_characteristic()

tarakan = tarakan.Tarakan(60, 600, 40, 20) #x, y, wight, hight
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

    if keys[pygame.K_LEFT]:
        player.hit_left()

    if keys[pygame.K_RIGHT]:
        player.hit_right()

    if keys[pygame.K_UP]:
        player.hit_up()

    if keys[pygame.K_DOWN]:
        player.hit_down()  
    
def get_damage(x, y, damage_area, health):
    if ( x > damage_area[0] ) and ( y > damage_area[1] ) and (  (damage_area[0] + damage_area[2]) > x  ) and (  (damage_area[1] + damage_area[3]) > y):
        health -= 1 
        print(health)
        return health





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

    if tarakan.health >= 0:
        pygame.draw.rect(win, tarakan.color, tarakan_characteristic)

    if player.cd != 0:
        player.damage()
        pygame.draw.rect(win, (0,0,255), player.damage_area, 5)

        tarakan.health = get_damage(tarakan.x, tarakan.y, player.damage_area, tarakan.health)




    pygame.display.update()
pygame.quit()