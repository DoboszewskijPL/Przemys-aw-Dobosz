import random
add_library('pdf')

def setup():
    global foto
    size(600, 600) # to nie są poporcje zdjęcia, zostaje nam kawałek niepotrzebnego tła, miało ybć wczytanie dowolnego zdjęcia dokumentowego, gdy wczytam większe - obecnie mi utnie
    foto = loadImage("Gemba.jpg")
    
    fill(200,255,200)


def draw():
    global foto
    image(foto, 0,0, 400, 514)
    if (key == CODED): # nie ma potrzeby powtarzać tego samego warunku, we wszystkim co jest pod nim wytabowane on obowiązuje
        clear() # zamiast pisać dwa razy lepiej było wynieść warunek wyżej
        beginRecord(PDF, "plik.pdf")
        image(foto, 0,0, 400, 514)
        if (keyCode == 37): # przydałąby się niedrukowalna na pdf'ie informacja dla użytkownika programu (który nie będzie widział kodu), jak to działa
            maska = createShape()
            maska.beginShape()
            maska.fill(215,0,0)
            maska.vertex(120,240)
            maska.vertex(75,210)
            maska.vertex(130,320)
            maska.vertex(200,340)
            maska.vertex(270,320)
            maska.vertex(325,210)
            maska.vertex(280,240)
            maska.endShape(CLOSE)
            shape(maska, 0,60)
            endRecord()
        if (keyCode == 39):
            wasy = createShape()
            wasy.beginShape()
            wasy.fill(0,0,0)
            wasy.vertex(150,280)
            wasy.vertex(200,270)
            wasy.vertex(250,280)
            wasy.endShape(CLOSE)
            shape(wasy, 0,60)
            endRecord()

def mousePressed():
    exit()
    
# uwagi nie są obowiązujące, ale możesz poćwiczyć poświęcając im nieco uwagi
# obecna wersja 1,75 (brakujące 0,25 byłoby za uporanie się z kwestią wczytywania uniwersalnie i w odpowiedniej proporcji)
