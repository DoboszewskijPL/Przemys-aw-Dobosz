class Pizza():
    ilosc_zamowien_na_pizze = 0
    def __init__(self, arg_x, arg_y, arg_r):
        self.rozmiar = 0
        self.rodzaj = False
        self.x = arg_x
        self.y = arg_y
        self.r = arg_r
        fill(150,75,0)
    def rysuj(self):
        arc(self.x, self.y, self.r, self.r, 0+radians(self.rozmiar+90), PI+ radians(self.rozmiar+90))
        arc(self.x, self.y, self.r, self.r, 0+radians(self.rozmiar+0), PI+ radians(self.rozmiar-90))
    def powieksz(self, stopnie):
        self.r += stopnie
    def zmien_rodzaj(self):
        Pizza.ilosc_zamowien_na_pizze +=1
        self.rodzaj = not self.rodzaj
        if self.rodzaj:
            fill(139,71,38)
        else:
            fill(150,75,0)
        
def setup():
    size(400, 400)
    global placek
    global placuszek
    beka = Pizza(width/2-50, height/2, 100)
    beczunia= Pizza(width/2+100, height/2, 100)
    
def mouseClicked():
    placek.zmien_rodzaj()
    placuszek.zmien_rodzaj()
def mouseWheel(event):
    placek.powieksz(5)
    placuszek.powieksz(5)
    print(placek.rozmiar)
    print(placuszek.rozmiar)
    
def draw():
    background(120)
    placek.rysuj()
    placuszek.rysuj()
    print(Pizza.ilosc_zamowien_na_pizze)
