import scene
class Player():
    def __init__(self, x, y, wight, hight, up, down, left, right):
        self.x = x
        self.y = y 
        self.hight = hight
        self.wight = wight
        self.color = (255, 0 , 0)

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
        

    
    
    def make_tuple_of_characteristic(self):
        tuple_of_characteristic = (self.x, self.y, self.wight, self.hight)
        return tuple_of_characteristic

        
