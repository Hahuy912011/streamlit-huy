class Game:
    money = 10000
    quantity = 0
    def __init__(self, name):
        self.name = name
        self.water = 0
        self.light = 0
        Game.quantity =+ 1
        Game.money -= 200
    
    @property
    def status(self): #trạng thái
        if (self.water == None and self.light == None):
            return "Đã bán"
        elif (self.water == 0 and self.light == 0):
            return "Nảy mầm"
        elif (self.water > 0 and self.light > 0 ):
            return "Sống"
        else:
            return "Chết"
     
    def gia_thanh(self): #giá thành
        if(self.water == None and self.light == None):
            return 0
        return max(0, self.water + self.light*10)
    
    @gia_thanh.setter
    def gia_thanh(self,value):
        nuoc_tang_them, 
        
