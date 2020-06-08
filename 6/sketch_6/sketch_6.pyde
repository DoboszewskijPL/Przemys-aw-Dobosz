class Kwadrat():
    def __init__(self, bok): # konstruktor jak się dowiedzieliśmy jest metodą prywatną, nie można go wywołać na obiekcie klasy po kropce, ani po za klasą
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): # dziedziczymy po klasie Kwadrat aby móć skorzystać z jej funkcjonalności
    def sketchPasiasty(self, x, y, paski): # dodajemy ilość pasków, w które ma być kwadrat
        Kwadrat.sketch(self, x, y) # korzystamy z metody klasy bazowej
        space = self.bok/paski # wyliczamy przerwęmiędzy paskami
        _xLinii_ = 0 # to jest pole chronione, nie powinno się go używać w kodzie po za klaą i klasami po niej dziedziczącymi 
        for pasek in range(0, paski): # dorysowujemy paski
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class WykresowyKwadrat(Kwadrat):
    def sketchWykresowy(self, x, y, kreski):
        Kwadrat.sketch(self, x, y)
        _xLinii_ = 0
        miejsce = self.bok/kreski
        _yLinii_ = 0
        for kreski in range(0, kreski):
            line(x+_xLinii_, y+_yLinii_, x+self.bok, y+_yLinii_)
            _xLinii_ += miejsce
            _yLinii_ += miejsce
def setup():
    size(800, 800)
    malyKwadrat = Kwadrat(50.0)
    malyKwadrat.sketch(200, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(100, 200)
    malyWykresowyKwadrat = WykresowyKwadrat(40)
    malyWykresowyKwadrat.sketchWykresowy(700,600, 5)
    wielkiWykresowyKwadrat = WykresowyKwadrat(350)
    wielkiWykresowyKwadrat.sketchWykresowy(200, 200, 83)
    
#1,75pkt
