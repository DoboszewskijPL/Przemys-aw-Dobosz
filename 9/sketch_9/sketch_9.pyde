def setup():
    size(800,600)
    global foto
    foto = loadImage("sh.png")
    noFill() # żeby nie przysłaniać obrazka
    strokeWeight(5) # bo nie zmieniasz w trakcie działąnia programu
    
def draw():
    global foto
    try:
        image(foto, 100, 100, 111, 106) # w try powinno się zawierać tylko to, co chcesz sprawdzić pod kątem błędu
    except:
        text("Twoje polecenie nie moze zostac wykonane. Na pocieszenie masz suchara: Dlaczego Dawid dobrze strzela? Bo Mysliwiec he he he", 60, 60)
        stroke(255, 0, 0)
    else:
        stroke(0,0,255)
    finally:
        rect(100, 100, 111, 106) # bo w obu przypadkach rysujemy ramkę
        
#1,5pkt
        
