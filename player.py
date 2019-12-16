import scene
import tarakan
import draw
import math

class Player():
    def __init__(self, x, y, wight, hight):
        self.x = x
        self.y = y 
        self.half_hight = hight/2
        self.half_wight = wight/2
        self.color = (255, 0 , 0)

        self.cd_max = 200
        self.td_max = 100 # td - это time damage. Функция перезарядки. td_max - это фактическая, а td - оставшаяся до следующего выстрела
        self.td = 0

        self.shoot_cd_max = 30
        self.shoot_cd = 0

        self.speed = 10

        self.direction_horizontal = 0
        self.direction_vertical = 0
        self.lazer = Lazer(self.x, self.y, self.direction_horizontal, self.direction_vertical)
        self.bullets = [] 

        self.health = 3

        self.weapon = -1

    def move_up(self):
        if self.y >=100:
            self.y -= self.speed
    def move_down(self):
        if self.y <= 950:
            self.y += self.speed
    def move_right(self):
        if self.x <= 960:
            self.x += self.speed
    def move_left(self):
        if self.x >= 20:
            self.x -= self.speed

    def tuple_of_characteristic(self):
        return (self.x-self.half_wight, self.y-self.half_hight, 2*self.half_wight, 2*self.half_hight)




            
    def damage_up(self):
        self.direction_vertical = -1
        self.direction_horizontal = 0
        self.shot()
    def damage_down(self):
        self.direction_vertical = 1
        self.direction_horizontal = 0
        self.shot()
    def damage_right(self):
        self.direction_vertical = 0
        self.direction_horizontal = 1
        self.shot()
    def damage_left(self):
        self.direction_vertical = 0
        self.direction_horizontal = -1
        self.shot()

    def shot(self):
            if self.weapon == 1:
                if self.td == 0:
                    self.td = self.td_max + self.cd_max
            else:
                if self.shoot_cd == 0:
                    self.shoot_cd = self.shoot_cd_max
                    bullet = Bullet(self.x, self.y, self.direction_horizontal, self.direction_vertical) 
                    self.bullets.append( bullet )


    

    def damage(self):
        if self.td != 0:
            self.lazer = Lazer(self.x, self.y, self.direction_horizontal, self.direction_vertical)
            self.td -= 1
        if self.shoot_cd != 0:
            self.shoot_cd -= 1 
        for bullet in self.bullets:
            bullet.move()
            if bullet.distance > bullet.distance_max:
                self.bullets.remove(bullet)





    def change_weapon(self):
        if self.td == 0:
            self.td = self.cd_max
            self.weapon = -self.weapon

    def get_damage(self, tarakan):
        if tarakan.stop_move == (tarakan.stop_move_max - 1) :
            self.health -= 1






        
class Bullet():
    def __init__(self, x, y, direction_horizontal, direction_vertical):
        self.x = x
        self.y = y

        self.speed = 10
        self.size = 5

        self.speed_x =  direction_horizontal * self.speed
        self.speed_y =  direction_vertical * self.speed 

        self.coordinates = ( self.x - self.size, self.y - self.size, 2*self.size, 2*self.size )

        self.distance = 0
        self.distance_max = 500
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.distance += self.speed  
        self.coordinates = ( self.x - self.size, self.y - self.size, 2*self.size, 2*self.size )
        print(self.distance)







class Lazer():
    def __init__(self, x, y, direction_horizontal, direction_vertical):
        self.wight_max = 100 # размер дамаг-площадки. Без _max -динамические величины, показывающие область дамага сейчас
        self.hight_max = 25

        self.x = (direction_horizontal)*abs(direction_horizontal-1)*self.wight_max - abs(direction_vertical)*self.hight_max +x
        self.y = (direction_vertical)*abs(direction_vertical-1)*self.wight_max - abs(direction_horizontal)*self.hight_max +y
        self.wight = 2*abs(direction_vertical)*self.hight_max + 2*abs(direction_horizontal)*self.wight_max
        self.high = 2*abs(direction_horizontal)*self.hight_max + 2*abs(direction_vertical)*self.wight_max

        self.wight_max = 100 # размер дамаг-площадки. Без _max -динамические величины, показывающие область дамага сейчас
        self.hight_max = 25

        self.coordinates = (self.x, self.y, self.wight, self.high)




