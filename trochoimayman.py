import random
class Game:
    def __init__(self, type):
        self.type = type
        self.score_list = []

    @property
    def score(self):
        if self.type == "xúc xắc":
            return random.randint(1,6)
        elif self.type == "đồng xu":
            return random.randint(0,1)

    @property
    def quantity(self):
        return len(self.score_list)

    @quantity.setter
    def quantity(self, new_quantity):
        for i in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.score_list = []
        
    @property
    def total_score(self):
        return sum(self.score_list)
        
        
    def play(self , quantity = 0):
        del self.quantity
        self.quantity = quantity

        print(f"Điểm của {self.quantity} lần gieo {self.type} là {self.score_list}")
        print(f"Tổng điểm: {self.total_score}")



game1 = Game(type = "đồng xu")
game1.play(10) 
game2 = Game(type = "xúc xắc")
game2.play(10)
