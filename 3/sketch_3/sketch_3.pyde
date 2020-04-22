def setup():
    size(800, 600)
    textSize(40)

def draw():
    if keyPressed:
        if (key == CODED):
            if (keyCode == 37):
                fill(255, 155, 0, 80)
        if (key == CODED):
            if (keyCode == 39):
                fill(255, 255, 255, 255)
    if keyPressed:
        if (key == 'd'):
            fill(255, 255, 255, 255)
    elif (mouseX > width/2-40) and (mouseX < width/2-20) and (mouseY > 260) and (mouseY < 300):
        fill(255, 155, 0, 80)
    else:
        fill(255,255,255,255)
        
    text("P", width/2-40, height/2)
    
    
    if keyPressed:
        if (key == CODED):
            if (keyCode == 39):
                fill(130,220,72,80)
            if (keyCode == 37):
                fill(255, 255, 255, 255)
        if (key == 'd'):
            fill(130,220,72,80)
    else:
        fill(255,255,255,255)
        
        
    text("D", width/2, height/2)
    
    s = createShape()
    s.beginShape()
    s.fill(0,0,255,255)
    s.stroke(0,0,255,255)
    s.vertex(300, height/2+70)
    s.vertex(330, height/2+50)
    s.vertex(width/2-40, height/2+60)
    s.vertex(width/2-10, height/2+40)
    s.vertex(width/2+100, height/2+90)
    s.endShape(CLOSE) # liczyłam na coś bardziej ozdobnego niż moje bazgroły ;)
    shape(s, 15, 0)
    
# nieźle, ale jest pewien mankament: zaznaczenie miało przekakiwać przy wybraniu strzałęk. U Ciebie same strzałki, gdy nic nie jest zaznaczone również podświetlają litery.
# zrealizowanie tego kryterium wymaga przebudowy logiki, więc wedle uznania, czy masz czas i chęci
# stan obecny: 1,75p
