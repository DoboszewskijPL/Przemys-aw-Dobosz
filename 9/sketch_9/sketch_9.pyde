def setup():
    size(800,600)
    global foto
    foto = loadImage("sh.png")
    
def draw():
    global foto
    try:
        rect(100, 100, 111, 106)
        stroke(0,0,255)
        strokeWeight(5)
        image(foto, 100, 100, 111, 106)
    except:
        text("Twoje polecenie nie moze zostac wykonana. Na pocieszenie masz suchara: Dlaczego Dawid dobrze strzela? Bo Mysliwiec he he he", 60, 60)
        stroke(255, 0, 0,)
        strokeWeight(5)
