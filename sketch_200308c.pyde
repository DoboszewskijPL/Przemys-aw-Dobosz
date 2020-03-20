def setup():
    size(1280,720)
def draw():
    if mousePressed:
        rect(width/100, mouseY, mouseX, 100, 100)
    else:
        clear()
