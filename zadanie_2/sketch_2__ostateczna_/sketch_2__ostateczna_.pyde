def setup():
    size(600,400)
    frameRate(60)
    global kolory
    rectMode(CENTER)
    kolory = {"ala":(255,0,0,80),"baba":(0,0,255,80), "cacy":(0,255,0,80), "dar":(255,0,120,80)}
    global i
    i=0
    global z
    z=0
    global b
    b=0
    global x
    x=height/2
    
def draw():
    background(0)
    global lista
    lista = []
    for klucz, wartosc in kolory.items():
        lista.append(wartosc)
    global i
    global z
    global b
    global x
    b+=2
    #stroke(255,0,0,80) # to jest zbędne powtórzenie 
    stroke(*kolory["baba"])
    rect(i, x, 100, height/2)
    if i==0 and x==height/2:
        z=1
    if i==300 and x==0:
        z=2
    if i==600 and x==200:
        z=3
    if i==300 and x==400:
        z=4
        
    if z==1:
        i+=3
        x-=2
        fill(*kolory["baba"])
    if z==2:
        i+=3
        x+=2
        fill(*kolory["ala"])
    if z==3:
        i-=3
        x+=2
        fill(*kolory["cacy"])
    if z==4:
        i-=3
        x-=2
        fill(*kolory["dar"])
    
    if mousePressed:
        exit()
        
# spróbuj nazywać zmienne tym co one robią, o wiele lepiej się taki kod czyta
# 2 pkt
