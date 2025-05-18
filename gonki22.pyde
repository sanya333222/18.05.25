img=0
uee=0
eee=0
x=1
w=1
u=1
def setup():
    size(400,600)
    global img
    global uee
    global eee
    img=loadImage("1.jpg")
    uee=loadImage("2.jpg")
    eee=loadImage("3.jpg")
def draw():
    global img
    global uee
    global eee
    global x
    global w
    global u
    image(img,x,200,100,100)
    image(uee,w,340,100,100)
    image(eee,u,470,100,100)
    x=x+1
    w=w+3
    u=u+2
