# globals
LIGHT_INDEX = 0
SIDES = None
RINGS=12
ANGLE = None
THETA = None
A = None
B = None

# constants
SPACING=1
WIDTH=90
HEIGHT=130

def setup_polygon(sides):
    global ANGLE, THETA, A, B, SIDES
    SIDES=sides
    ANGLE=360.0/SIDES
    THETA=(180-ANGLE)/2

    A=SPACING*1.2
    B=abs(2*A*cos(radians(THETA)))
    noStroke()

def draw_polygon(sides):
    global LIGHT_INDEX
    setup_polygon(sides)

    # draw outermost rings first
    for ring in range(RINGS,0,-1):
        # draw sides
        for n in range(0,sides):
            # setup the side's coordinate system
            pushMatrix()
            rotate(radians(ANGLE*n))
            translate(-A*ring,0)
            # ellipse(0,0,SPACING,SPACING)
            rotate(radians(90-THETA))

            # setup color
            fill(360/sides*n,40,100)

            # draw a side
            # do this with a half SPACING gap
            for i in range(0,ring):
                translate(0,-B/2)
                # text(LIGHT_INDEX,0,0)
                ellipse(0,0,1,1)
                x = modelX(0,0,0)
                y = modelY(0,0,0)
                z = modelZ(0,0,0)
                # print(str(LIGHT_INDEX)+": ["+str(x)+", "+str(y)+"]")
                translate(0,-B/2)

                LIGHT_INDEX += 1
            popMatrix() # reset coordinate system

def setup():
    size(WIDTH,HEIGHT,P3D)
    colorMode(HSB,360,100,100)
    noStroke()
    fill(0,0,100)

def draw():
    global LIGHT_INDEX, ANGLE, THETA
    LIGHT_INDEX = 0

    background(color(0,0,0))
    # rotateX(radians(300))
    translate(width/2,height/2)
    # ellipse(0,0,SPACING,SPACING)

    # print(frameRate)


    #####
    # 1 #
    #####
    pushMatrix()
    translate(0,SPACING*30*1.5)         # position center
    # text("1",0,0)
    rotate(radians(90-360/5)) # align with neighbor
    rotate(radians(360/5*3)) # rotate input
    rotate(radians(360/5/2)) # rotate input
    draw_polygon(5)
    popMatrix()

    # #####
    # # 2 #
    # #####
    pushMatrix()
    # rotateY(radians(30))
    # translate(210,0)
    translate(0,SPACING*30*0.5)         # position center
    # text("2",0,0)
    rotate(radians(360/6*5)) # rotate input
    draw_polygon(6)
    popMatrix()
    
    # #####
    # # 3 #
    # #####
    pushMatrix()
    translate(0,-SPACING*30*0.5)
    # text("3",0,0)
    rotate(radians(360/6*4)) # rotate input
    draw_polygon(6)
    popMatrix()

    # #####
    # # 4 #
    # #####
    pushMatrix()
    translate(0,-SPACING*30*1.5)         # position center
    # text("4",0,0)
    rotate(radians(90-360/5)) # align with neighbor
    rotate(radians(360/5*4)) # rotate input
    # rotate(radians(360/5/2)) # rotate input
    draw_polygon(5)
    popMatrix()

    # #####
    # # 5 #
    # #####
    pushMatrix()
    # rotateY(radians(30))
    # translate(210,0)
    translate(-SPACING*30*0.9,SPACING*30)         # position center
    # text("5",0,0)
    rotate(radians(360/6*4)) # rotate input
    draw_polygon(6)
    popMatrix()

    # #####
    # # 6 #
    # #####
    pushMatrix()
    translate(-SPACING*30*0.9,0)         # position center
    # text("6",0,0)
    rotate(radians(180)) # align with neighbor
    # rotate(radians(360/5*4)) # rotate input
    rotate(radians(360/5)) # rotate input
    draw_polygon(5)
    popMatrix()

    # #####
    # # 7 #
    # #####
    pushMatrix()
    translate(-SPACING*30*0.9,-SPACING*30)         # position center
    # text("7",0,0)
    rotate(radians(360/6*4)) # rotate input
    draw_polygon(6)
    popMatrix()

    # #####
    # # 8 #
    # #####
    pushMatrix()
    translate(SPACING*30*0.9,SPACING*30)         # position center
    # text("8",0,0)
    rotate(radians(360/6*5)) # rotate input
    draw_polygon(6)
    popMatrix()

    
    # #####
    # # 9 #
    # #####
    pushMatrix()
    translate(SPACING*30*0.9,0)         # position center
    # text("9",0,0)
    # rotate(radians(180)) # align with neighbor
    rotate(radians(360/5*4)) # rotate input
    # rotate(radians(360/5)) # rotate input
    draw_polygon(5)
    popMatrix()

    # ######
    # # 10 #
    # ######
    pushMatrix()
    translate(SPACING*30*0.9,-SPACING*30)         # position center
    # text("10",0,0)
    rotate(radians(360/6*5)) # rotate input
    draw_polygon(6)
    popMatrix()

    fill(360,0,100)
    # text("X: "+str(mouseX%360)+"\nY: "+str(mouseY%360),-width/2+20,-height/2+20)
    noStroke()