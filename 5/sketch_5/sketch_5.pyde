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
    global placki
    placek = Pizza(width/2-80, height/2, 100)
    placuszek= Pizza(width/2+100, height/2, 100)
    placki = (placek, placuszek) # warto agregować w kolekcję, gdy jest więcej obiektów

    
def mouseClicked():
    for placek in placki:
        placek.zmien_rodzaj()
def mouseWheel(event):
    placki[0].polacz(15)
    placki[1].polacz(-15)
    for placek in placki:
        print(placek.laczenie)
    
def draw():
    background(120)
    for placek in placki:
        placek.rysuj()
        
# 1,75p; metody są  kalką działania moich, można było wynyśleć inne działanie
