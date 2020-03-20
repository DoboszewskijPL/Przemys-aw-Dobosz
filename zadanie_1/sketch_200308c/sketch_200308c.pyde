def setup():
    size(1280,720)
def draw():
    if mousePressed:
        rect(width/100, mouseY, mouseX, 100, 100) # po za width analogicznie działa height
    else:
        clear()
        
#tak, o to chodziło :)
#2pkt
