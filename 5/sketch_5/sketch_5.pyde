class Pizza():
    def __init__(self, arg_x, arg_y, arg_r):
        self.laczenie = 0
        self.rodzaj = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
        fill(150,75,0)
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.laczenie+90), PI+ radians(self.laczenie+90))
    def polacz(self, stopnie):
        self.laczenie += stopnie
        self.x += stopnie
    def zmien_rodzaj(self):
        self.rodzaj = not self.rodzaj
        if self.rodzaj:
            fill(139,71,38)
        else:
            fill(150,75,0)
        
def setup():
    size(400, 400)
    global placek
    global placuszek
    placek = Pizza(width/2-80, height/2, 100)
    placuszek= Pizza(width/2+100, height/2, 100)
    
def mouseClicked():
    placek.zmien_rodzaj()
    placuszek.zmien_rodzaj()
def mouseWheel(event):
    placek.polacz(15)
    placuszek.polacz(-15)
    print(placek.laczenie)
    print(placuszek.laczenie)
    
def draw():
    background(120)
    placek.rysuj()
    placuszek.rysuj()
