import scene
import player
import random
import math

#после смерти экземпляр класса таракана не удаляется, а с ним просто всё перестаёт взаимодействовать. Нужно прописать if

class Tarakan():
    def __init__(self, x, y, wight, hight, HP, speed):
        self.x = x
        self.y = y 
        self.half_hight = hight /2
        self.half_wight = wight /2
        self.color = (0, 255 , 0)

        self.speed = speed
        self.stop_move = 0 # Переменная остановки движения. После того, как таракан нанёс урон игроку, он останавливается, и переменная становится ненулевой
        self.stop_move_max = 100
        self.damage_radius = 10 # Радиус дамага таракана

        self.static_move_count = 0

        self.health = HP

    def tuple_of_characteristic(self):
        return (self.x-self.half_wight, self.y-self.half_hight, 2*self.half_wight, 2*self.half_hight) 

    def dinamics(self, player):
        if player.td > (player.cd_max *player.weapon): #Тут, конечно, дикий костыль
            self.get_damage(player)
        self.move(player)

    def move(self, player):
        if self.stop_move == 0:
            r = ( (player.x - self.x)**2 + (self.y - player.y)**2 )**0.5
            if r < self.damage_radius:
                self.stop_move = self.stop_move_max
            self.x += self.speed * (player.x - self.x) / r
            self.y += self.speed * (player.y - self.y) / r
        else:
            self.stop_move -= 1

    def get_damage(self, player):
        for damage_point in player.damage_area:
            if ( self.x > damage_point[0] - self.half_wight ) and ( self.y > damage_point[1] - self.half_hight ) and (  (damage_point[0] + damage_point[2] + self.half_wight ) > self.x  ) and (  (damage_point[1] + damage_point[3] + self.half_hight) > self.y):
                self.health -= 1





        '''
        прерывистое движение:
        if t < 70:
            self.x += random.randint(-100, 100)
            self.y += random.randint(-100, 100)
            t = 0
        else:
            t += 1

        

    def move_vertical(self):
        self.x += random.randint(-100,100)

    
    def move_up(self):
        if self.y >=510:
            self.y -= self.speed
            self.static_move_count +=1
        else:
            self.static_move_count = 20

    def move_down(self):
        if self.y <= 950:
            self.y += self.speed
            self.static_move_count +=1
        else:
            self.static_move_count = 11

    def move_right(self):
        if self.x <= 960:
            self.x += self.speed
            self.static_move_count +=1

    def move_left(self):
        if self.x >= 20:
            self.x -= self.speed
            self.static_move_count +=1




    
    if find player is false

    def move_behavior(self, player_x, player_y):
        if direction == 1:
            if self.static_move_count <=10:
                self.move_down
            
            if  self.static_move_count >10 and self.static_move_count <=20:
                self.move_up
                if self.static_move_count == 20:
                    self.static_move_count = 0 '''



        

        


