def setup():
    size(600,400)
    frameRate(5)
    global kolory
    rectMode(CENTER)
    
    kolory = {"czerwony":(255,0,0,80),"niebieski":(0,0,255,80), "zielony":(0,255,0,80)}
    global i
    i=0
    global z
    z=0
    global b
    b=0
def draw():
    
    global lista
    lista = []
    for klucz, wartosc in kolory.items():
        lista.append(wartosc)
    global i
    global z
    global b
    b+=2
    
    stroke(*kolory["niebieski"])
    fill(*lista[b%len(lista)])
    rect(i, height/2, 100, height/2)
    if i==0:
        z=1
    if i==600:
        z=2
        
    if z==1:
        i+=2
    if z==2:
        i-=2
    
    if mousePressed:
        exit()
