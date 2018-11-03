# globals
LIGHT_INDEX = 0
SIDES = None
RINGS=12
ANGLE = None
THETA = None
A = None
B = None

# constants
WIDTH=700
HEIGHT=860

CIRCLE_DIAMETER=5

def setup_polygon(sides):
    global ANGLE, THETA, A, B, SIDES
    SIDES=sides
    ANGLE=360.0/SIDES
    THETA=(180-ANGLE)/2

    A=10
    B=abs(2*A*cos(radians(THETA)))

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
            # ellipse(0,0,CIRCLE_DIAMETER,CIRCLE_DIAMETER)
            rotate(radians(90-THETA))

            # setup color
            fill(360/sides*n,40,100)

            # draw a side
            # do this with a half SPACING gap
            for i in range(0,ring):
                translate(0,-B/2)
                # text(LIGHT_INDEX,0,0)
                ellipse(0,0,CIRCLE_DIAMETER,CIRCLE_DIAMETER)
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
    ellipse(0,0,CIRCLE_DIAMETER,CIRCLE_DIAMETER)

    # print(frameRate)


    #####
    # 1 #
    #####
    pushMatrix()
    rotate(radians(90-360/5)) # align with neighbor
    translate(0,-230)         # position center
    rotate(radians(-360/6*5)) # rotate input
    text("1",0,0)
    # draw_polygon(6)
    popMatrix()

    #####
    # 2 #
    #####
    pushMatrix()
    rotateY(radians(30))
    translate(210,0)
    text("2",0,0)
    draw_polygon(5)
    popMatrix()
    
    #####
    # 3 #
    #####
    pushMatrix()
    rotate(radians(90-360/5*4)) # align with neighbor
    translate(0,-230)           # position center
    rotate(radians(360/6*2))    # rotate input
    text("3",0,0)
    # draw_polygon(6)
    popMatrix()


    #####
    # 4 #
    #####
    pushMatrix()
    # position into "5" spot
    dihedral_5 = -acos(sqrt(5)/3)
    rotateX(-dihedral_5/2)
    translate(0,-120)
    # position into "4" spot
    dihedral_4 = radians(30)
    rotateX(dihedral_4/2)
    translate(0,-265)
    # final alignment
    rotate(radians(90-360/5))
    rotate(radians(360/5))
    text("4",0,0)
    draw_polygon(5)
    popMatrix()

    #####
    # 5 #
    #####
    pushMatrix()
    # position into "5" spot
    dihedral_5 = -acos(sqrt(5)/3)
    rotateX(-dihedral_5/2)
    translate(0,-125)
    # final alignment
    rotate(radians(360/6))
    text("5",0,0)
    draw_polygon(6)
    popMatrix()

    #####
    # 6 #
    #####
    pushMatrix()
    # position into "6" spot
    dihedral_6 = -acos(sqrt(5)/3)
    rotateX(dihedral_6/2)
    translate(0,125)
    # final alignment
    rotate(radians(360/6*5))
    text("6",0,0)
    draw_polygon(6)
    popMatrix()

    #####
    # 7 #
    #####
    pushMatrix()
    # position into "6" spot
    dihedral_6 = -acos(sqrt(5)/3)
    rotateX(dihedral_6/2)
    translate(0,120)
    # position into "7" spot
    # dihedral_7 = acos(-1.0/15*sqrt(75+30*sqrt(5)))
    # rotateX((dihedral-7 - dihedral_6)/2)
    dihedral_7 = radians(-30)
    rotateX(dihedral_7/2)
    translate(0,265)
    # final alignment
    rotate(radians(90-360/5/2))
    rotate(radians(360/5*3))
    text("7",0,0)
    draw_polygon(5)
    popMatrix()

    #####
    # 8 #
    #####
    pushMatrix()
    translate(-190,0)         # position center
    rotate(radians(90+360/5)) # align with neighbor
    translate(0,230)         # position center
    rotate(radians(-360/6)) # rotate input
    text("8",0,0)
    draw_polygon(6)
    popMatrix()

    
    #####
    # 9 #
    #####
    pushMatrix()
    rotateY(radians(-30))
    translate(-210,0)
    # final alignment
    rotate(radians(180)) # rotate input
    text("9",0,0)
    draw_polygon(5)
    popMatrix()

    ######
    # 10 #
    ######
    pushMatrix()
    translate(-180,200,-100)         # position center
    # rotate(-360/6/2)
    # rotateX(radians(-mouseX%360))
    # rotateY(radians(-mouseY%360))
    # rotateX(radians(-228))
    # rotateY(radians(-186))
    scale(0.8)
    # rotate(radians(10))
    # shearY(radians(27))
    shearX(radians(192))
    shearY(radians(mouseX%360))
    # rotate(radians(90-360/5)) # align with neighbor
    rotate(radians(360/6*4))  # rotate input
    text("10",0,0)
    draw_polygon(6)
    popMatrix()

    fill(360,0,100)
    text("X: "+str(mouseX%360)+"\nY: "+str(mouseY%360),-width/2+20,-height/2+20)
    noStroke()