import scene
import player_config
import random
import math


class Tarakan():
    def __init__(self, x, y, characteristic):
        self.x = x
        self.y = y

        self.type = characteristic[0]
  
        self.half_hight = characteristic[2] /2
        self.half_wight = characteristic[1] /2
        self.color = characteristic[5]

        self.speed = characteristic[4]
        self.stop_move = 0 # Переменная остановки движения. После того, как таракан нанёс урон игроку, он останавливается, и переменная становится ненулевой
        self.stop_move_max = 100
        self.damage_radius = 10 # Радиус дамага таракана

        self.static_move_count = 0

        self.health = characteristic[3]

        self.jump_speed_x = 0
        self.jump_speed_y = 0
        self.jump_duration = characteristic[6]
        self.jump_cd = characteristic[7]
        self.jump_speed = characteristic[8]
        self.jump_time = self.jump_duration + self.jump_cd


    def coordinates(self):
        return (self.x-self.half_wight, self.y-self.half_hight, 2*self.half_wight, 2*self.half_hight) 

    def dinamics(self, player):
        if player.td > (player.cd_max *player.weapon): #Тут, конечно, дикий костыль
            self.get_damage(player)
        self.move(player)

    def move(self, player):
        if self.stop_move == 0:
            r = ( (player.x - self.x)**2 + (self.y - player.y)**2 )**0.5
            if ( abs(self.x - player.x) < player.half_wight + self.half_wight ) and ( abs(self.y - player.y) < player.half_hight + self.half_hight ):
                self.stop_move = self.stop_move_max
            self.jump()
            self.x += self.speed * (player.x - self.x) / r + self.jump_speed_x
            self.y += self.speed * (player.y - self.y) / r + self.jump_speed_y
        else:
            self.stop_move -= 1


    def get_damage(self, player):
        if ( self.x > player.lazer.coordinates[0] - self.half_wight ) and ( self.y > player.lazer.coordinates[1] - self.half_hight ) and (  (player.lazer.coordinates[0] + player.lazer.coordinates[2] + self.half_wight ) > self.x  ) and (  (player.lazer.coordinates[1] + player.lazer.coordinates[3] + self.half_hight) > self.y) and (player.weapon == 1):
                self.health -= 5
        for bullet in player.bullets:
            if ( self.x > bullet.coordinates[0] - self.half_wight ) and ( self.y > bullet.coordinates[1] - self.half_hight ) and (  (bullet.coordinates[0] + bullet.coordinates[2] + self.half_wight ) > self.x  ) and (  (bullet.coordinates[1] + bullet.coordinates[3] + self.half_hight) > self.y):
                self.health -= 30
                player.bullets.remove(bullet)


    def jump(self):
        if self.jump_time == self.jump_duration:
            fi = random.random()*2*math.pi
            self.jump_speed_x = self.jump_speed*math.cos(fi)
            self.jump_speed_y = self.jump_speed*math.sin(fi)
        elif self.jump_time == 0:
            self.jump_speed_x = 0
            self.jump_speed_y = 0
            self.jump_time = self.jump_duration + self.jump_cd
        self.jump_time -= 1
        if ( self.x > 980 - self.half_wight ) or ( self.x < 5 + self.half_wight ):
            self.jump_speed_x = -self.jump_speed_x
        if ( self.y > 980 - self.half_hight ) or ( self.y < 100 + self.half_hight ):
            self.jump_speed_y = -self.jump_speed_y

        



