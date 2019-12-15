import scene
import player
import random
import math

#после смерти экземпляр класса таракана не удаляется, а с ним просто всё перестаёт взаимодействовать. Нужно прописать if

class Tarakan():
    def __init__(self, x, y, wight, hight, HP):
        self.x = x
        self.y = y 
        self.hight = hight
        self.wight = wight
        self.color = (0, 255 , 0)
        self.speed = 1


        self.static_move_count = 0

        self.health = HP

    def tuple_of_characteristic(self):
        return (self.x, self.y, self.wight, self.hight) 


    def move(self, player):
        r = ( (player.x - self.x)**2 + (self.y - player.y)**2 )**0.5
        print(r)
        self.x += self.speed * (player.x - self.x) / r
        self.y += self.speed * (player.y - self.y) / r

    def get_damage(self, player):
        if ( self.x > player.damage_area[0] ) and ( self.y > player.damage_area[1] ) and (  (player.damage_area[0] + player.damage_area[2]) > self.x  ) and (  (player.damage_area[1] + player.damage_area[3]) > self.y):
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




    
    def hit_player():
        pass


    if find player is false

    def move_behavior(self, player_x, player_y):
        if direction == 1:
            if self.static_move_count <=10:
                self.move_down
            
            if  self.static_move_count >10 and self.static_move_count <=20:
                self.move_up
                if self.static_move_count == 20:
                    self.static_move_count = 0 '''



        

        


