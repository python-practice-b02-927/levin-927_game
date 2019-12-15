import scene

class Player():
    def __init__(self, x, y, wight, hight):
        self.x = x
        self.y = y 
        self.hight = hight
        self.wight = wight
        self.color = (255, 0 , 0)

        self.cd_max = 100 # cd - это cool down. Функция перезарядки. сd_max - это фактическая, а cd - оставшаяся до следующего выстрела
        self.cd = 0

        self.damage_high_max = 50 # размер дамаг-площадки. Без _max -динамические величины, показывающие область дамага сейчас
        self.damage_length_max = 200

        self.speed = 10

    def move_up(self):
        if self.y >=510:
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

    def hit_up(self):
        if self.cd == 0:
            self.cd = self.cd_max
            self.damage_x = - self.damage_high_max / 2
            self.damage_y= - self.damage_length_max
            self.damage_length = self.damage_high_max
            self.damage_high = self.damage_length_max
    def hit_down(self):
        if self.cd == 0:
            self.cd = self.cd_max
            self.damage_x = -self.damage_high_max /2
            self.damage_y= 0
            self.damage_length = self.damage_high_max
            self.damage_high = self.damage_length_max
    def hit_right(self):
        if self.cd == 0:
            self.cd = self.cd_max
            self.damage_x = 0
            self.damage_y= -self.damage_high_max /2
            self.damage_length = self.damage_length_max
            self.damage_high = self.damage_high_max
    def hit_left(self):
        if self.cd == 0:
            self.cd = self.cd_max
            self.damage_x = -self.damage_length_max
            self.damage_y= - self.damage_high_max /2
            self.damage_length = self.damage_length_max
            self.damage_high = self.damage_high_max

    def damage(self):
        self.cd -= 1
        self.damage_area = (self.x + self.damage_x, self.y + self.damage_y, self.damage_length, self.damage_high )



   

    
    
    def make_tuple_of_characteristic(self):
        tuple_of_characteristic = (self.x, self.y, self.wight, self.hight)
        return tuple_of_characteristic

        
