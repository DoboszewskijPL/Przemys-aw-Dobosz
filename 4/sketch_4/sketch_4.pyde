add_library('pdf')

def setup():
    global foto
    size(400, 400) # ustawiamy wielkość okna
    foto = loadImage("Gemba.jpg")
    beginRecord(PDF, "plik.pdf")
    
    fill(200,255,200) # ustawiamy wypełnienie dla kształtów


def draw():
    global foto
    image(foto, 0,0, height, width)
    
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
    shape(maska, 0,0)
    
    #wasy = createShape()
    #wasy.beginShape()
    #wasy.fill(0,0,0)
    #wasy.vertex(150,280)
    #wasy.vertex(200,270)
    #wasy.vertex(250,280)
    #wasy.endShape(CLOSE)
    #shape(wasy, 0,0)
    
    endRecord()

def mousePressed():
    exit()
    
# wybór między maską a wąsami powinien być możliwy w trakci działąnia programu, a więc poprzez jakieś UI wystawione do użytkownika.
# zdjęcie dokumentowe ma swoje proporcje, któe zatraciłęś dostosowując do okna, które jest innych proporcji i twarz przez to wygląda nienaturalnie
# obecna wersja 1,5pkt
