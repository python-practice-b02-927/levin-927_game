import scene
import player

class Tarakan():
     def __init__(self, x, y, wight, hight, up, down, left, right):
        self.x = x
        self.y = y 
        self.hight = hight
        self.wight = wight
        self.color = (240, 0 , 0)
        self.speed = 10
        self.direction = random.randint(0, 1)
        """самый простой выбор. 
        не хочу мучиться со случайным движением с выделенным направлением
        если 0 то по х, если 1 - по у"""
        
        self.static_move_count = 0

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

    def check_player(self, player_x, player_y):
        if player_x == 0:
            pass
    def fight():
        pass

    def get_damage():
        pass
    
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
                    self.static_move_count = 0"""
        

        


