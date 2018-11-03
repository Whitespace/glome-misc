add_library('artnet4j')

# globals
LIGHT_INDEX = 0
SIDES = None
RINGS=12
ANGLE = None
THETA = None
A = None
B = None

# constants
WIDTH=72
HEIGHT=72

CIRCLE_DIAMETER=1

PIXLITE_IP='192.168.1.2'
LIGHTS_PER_UNIVERSE=170
STAR_COUNT=390*1 + 468*0
artnet = ArtNetClient()
galaxy = []
dmxData = [None] * STAR_COUNT * 3

def setup_polygon(sides):
    global ANGLE, THETA, A, B, SIDES
    SIDES=sides
    ANGLE=360.0/SIDES
    THETA=(180-ANGLE)/2

    A=3
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
            fill(100/sides*n,40,100)

            # draw a side
            # do this with a half SPACING gap
            for i in range(0,ring):
                translate(0,-B/2)
                # text(LIGHT_INDEX,0,0)
                ellipse(0,0,CIRCLE_DIAMETER,CIRCLE_DIAMETER)
                x = modelX(0,0,0)
                y = modelY(0,0,0)
                z = modelZ(0,0,0)
                galaxy[LIGHT_INDEX].x = x
                galaxy[LIGHT_INDEX].y = y
                print(str(LIGHT_INDEX)+": ["+str(x)+", "+str(y)+"]")
                translate(0,-B/2)
                galaxy[LIGHT_INDEX].h = 100/sides*n/100.0
                LIGHT_INDEX += 1
            popMatrix() # reset coordinate system

class Star:
    def __init__(self):
        self.h = random(0,1)
        self.s = 1.0
        self.b = 1.0
        self.x = None
        self.y = None
        # self.b = 0.01176471

def fractalNoise(x, y, z):
    r = 0.0
    amp = 1.0
    for octave in range(0,4):
        r += noise(x, y, z) * amp
        amp /= 2
        x *= 2
        y *= 2
        z *= 2
    return r

def setup():
    global y,indexPosition,num,xs,ys
    y=0
    indexPosition=0
    num=50
    xs=[0]*num
    ys=[0]*num

    global dx, dy
    dx=dy=0
    
    size(WIDTH,HEIGHT,P3D)
    colorMode(HSB,100)
    noStroke()
    fill(0,0,100)

    # create stars
    for i in range(0, STAR_COUNT):
        galaxy.append(Star())
    noStroke()

    # start server
    artnet.start()

def draw():
    global dx, dy
    now = millis()
    speed = 0.05
    angle = sin(now * 0.001)
    z = now * 0.00008
    hue = now * 0.01
    scale = 0.015

    dx += cos(angle) * speed
    dy += sin(angle) * speed

    # loadPixels()
    # for x in range(0, width):
    #     for y in range(0, height):
     
    #         n = fractalNoise(dx + x*scale, dy + y*scale, z) - 0.75
    #         m = fractalNoise(dx + x*scale, dy + y*scale, z + 10.0) - 0.75

    #         c = color(
    #             (hue + 80.0 * m) % 100.0,
    #             100 - 100 * constrain(pow(3.0 * n, 3.5), 0, 0.9),
    #             100 * constrain(pow(3.0 * n, 1.5), 0, 0.9))
     
    #         pixels[x + width*y] = c
    # updatePixels()

    global LIGHT_INDEX, ANGLE, THETA
    LIGHT_INDEX = 0

    # rotateX(radians(300))
    translate(WIDTH/2,HEIGHT/2)

    colorMode(HSB,100)
    draw_polygon(5)
    # draw_polygon(6)

    ################
    # pulsing line #
    ################
    # background(0)
    # translate(-width/2,-height/2)  # reset x,y to home
    # global y
    # colorMode(HSB,1.0,1.0,1.0)
    # stroke(1.0)
    # strokeWeight(height/10.0)
    # line(0,y,width,y)
    # y+=2
    # y%=height*1.1

    ###################
    # rainbow circles #
    ###################
    # hue = height*2
    # colorMode(HSB, hue, 1.0, 1.0)
    # for y in range(height,0,-1):
    #     fill((y + frameCount*2) % hue, 1, 1)
    #     ellipse(0,0,y,y)
    
    ####################
    # rainbow gradient #
    ####################
    # translate(-width/2,-height/2)  # reset x,y to home
    # hue = height*2
    # colorMode(HSB, hue, 1.0, 1.0)
    # strokeWeight(1)
    # for y in range(0,height):
    #     stroke((y + frameCount*2) % hue, 1, 1)
    #     line(0, y, width, y)

    ############
    # pinwheel #
    ############
    # background(0)
    # # resetMatrix()
    # # translate(width/2,height/2)  # reset x,y to home
    # colorMode(HSB, 360, 1.0, 1.0)
    # fill(0,0,0)
    # ellipse(0,0,height,height)
    # # ellipse(0,0,height,height)
    # # for n in range(0,2):
    # speed = frameCount*7
    # fill(frameCount % 360, 1, 1)
    # arc(0,0,height,height,radians(speed),radians(speed+60),PIE)


    ####################
    # trailing circles #
    ####################
    # fill(1,1,1)
    # global indexPosition,num,xs,ys
    # xs[indexPosition] = mouseX
    # ys[indexPosition] = mouseY
    # # Cycle between 0 and the number of elements
    # indexPosition = (indexPosition + 1) % num
    # for i in range(0,num):
    #     # Set the array position to read
    #     pos = (indexPosition + i) % num
    #     radius = (num-i)*1.5
    #     ellipse(xs[pos], ys[pos], radius, radius)

    #########################
    # send data over ArtNet #
    #########################
    colorMode(HSB, 1.0, 1.0, 1.0)
    for universe, i in enumerate(range(0, len(galaxy), LIGHTS_PER_UNIVERSE)):
        stars = galaxy[i:i+LIGHTS_PER_UNIVERSE]
        for j, star in enumerate(stars):
            pos = i + j
            c = get(int(star.x),int(star.y))
            # c = color(star.h, star.s, star.b)
            # I think these are coming out as signed integers so I can't use 255
            dmxData[pos*3 + 0] = int(red(c)*127)
            dmxData[pos*3 + 1] = int(green(c)*127)
            dmxData[pos*3 + 2] = int(blue(c)*127)
        # broadcast
        artnet.unicastDmx(PIXLITE_IP, 0, universe, dmxData[i*3:(i+LIGHTS_PER_UNIVERSE)*3])
        # print("universe: " + str(universe) + " range: " + str(i*3) + ".." + str((i+LIGHTS_PER_UNIVERSE)*3))
    colorMode(HSB,100)