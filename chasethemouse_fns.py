# Basic mouse interaction

from buttondemo import makeButton, inButton
from graphics import *
import math
from typing import Callable, List

def makeHead(r:float, color:str) -> Circle:
    # Pre: color is a color specification AND
    assert r > 0
    head:Circle = Circle(Point(0, 0), r)
    head.setFill(color)
    head.setOutline(color)
    # Post: head has fillColor == color and outline color == color AND
    assert (type(head) is Circle) \
        and head.getCenter().getX() == 0 and head.getCenter().getY() == 0
    return head

def makeMouseEar(r:float, angle:float) -> Circle:
    # Pre: angle is an angle in radians
    assert r > 0
    earPt:Point = Point(1.3 * r * math.cos(angle),
                        1.3 * r * math.sin(angle))
    ear:Circle = Circle(earPt, r * .5)
    ear.setFill('gray')
    ear.setOutline('gray')
    # Post: ear's fill color == gray and ear's outline color == gray AND
    assert ear.getRadius() == r * .5 and \
        ear.getCenter().getX() == 1.3 * r * math.cos(angle) and \
        ear.getCenter().getY() == 1.3 * r * math.sin(angle)
    return ear

def makeEye(angle:float, r:float, color:str) -> Oval:
    # Pre: angle is in radians and color specifies a color AND
    assert r > 0
    lowerPt:Point = Point(0, r * -0.2)
    upperPt:Point = Point(r * math.cos(angle), r * math.sin(angle))
    eye:Oval = Oval(lowerPt, upperPt)
    eye.setFill(color)
    # Post: The bounding box of eye is the bounding box specified by
    #   lowerPt and upperPt AND eye's fill color == color
    return eye

def makeEyeList(r:float, color:str) -> List[GraphicsObject]:
    # Pre: color is a color specification AND
    assert r > 0
    eyelist:List[GraphicsObject] = []
    for i in range(2):
        angle:float = math.radians(50) + i * math.radians(80)
        eyelist.append(makeEye(angle, r, color))
    # Post:
    assert (len(eyelist) == 2) and (type(eyelist[0]) is Oval) and \
        (type(eyelist[1]) is Oval)
    # type assertions because mypy can't check for Ovals here, only
    #   for GraphicsObjects
    return eyelist

def makeMouthPart(centerPt:Point, r:float, angle:float) -> Line:
    endPt:Point = Point(centerPt.getX() + 0.5 * r * math.cos(angle),
                        centerPt.getY() + 0.5 * r * math.sin(angle))
    mouthPart:Line = Line(centerPt, endPt)
    return mouthPart

def makeMouth(radius:float) -> List[GraphicsObject]:
    # Mouth
    # BROKEN. The side of the mouth with i == 1 is bigger than the side with i == 0.
    mouthList:List[GraphicsObject] = []
    for i in range(2):
        angle = math.radians(330) - i * math.radians(120)
        meeting:Point = Point(0, -0.35 * radius)
        mouthList.append(makeMouthPart(meeting, radius, angle))
    return mouthList

def makeWhisker(angle:float, r:float) -> Line:
    # Make and return a line representing a whisker.  The line is radial
    # to the animal's head.  angle is the angle along which the whisker lies.
    inFactor:float = 0.9   # How far the inside end is from the center, as a factor of r
    outFactor:float = 1.6  # How far the outside end is from the center, as a factor of r

    innerEnd:Point = Point(inFactor * r * math.cos(angle), inFactor * r * math.sin(angle))
    outerEnd:Point = Point(outFactor * r * math.cos(angle), outFactor * r * math.sin(angle))

    whisker:Line = Line(innerEnd, outerEnd)
    return whisker

def makeWhiskerList(r:float) -> List[GraphicsObject]:
    # Make and return a list of Whiskers
    whiskerList:List[GraphicsObject] = []
    for j in range(2):
        for i in range(-1, 2):
            angle = math.radians(0) + i * math.radians(8) + j * math.pi
            whiskerList.append(makeWhisker(angle, r))
    return whiskerList

def makeMouse() -> List[GraphicsObject]:
    radius:float = 0.05
    rodent:List[GraphicsObject] = [] # Empty list
    rodent.append(makeHead(radius, 'gray'))

    # Ears
    for i in range(2):
        angle = (math.pi/3) + i * (math.pi/3)
        rodent.append(makeMouseEar(radius, angle))

    rodent.extend(makeEyeList(radius, 'black'))
    rodent.extend(makeMouth(radius))
    rodent.extend(makeWhiskerList(radius))
            
    return rodent

def makeCatEar(centralAngle:float, r:float, color:str) -> Polygon:
    # Make and return a triangle representing the ear of the cat.  The centralAngle
    # is the angle of the outer tip of the ear.  r is the radius of the cat's head,
    # and color is the color of the cat's head.
    tipFactor:float = 1.8 # How far the tip is from the center of the head, compared to r
    tip:Point = Point(tipFactor * r * math.cos(centralAngle), tipFactor * r * math.sin(centralAngle))
    earSpreadAngle:float = math.radians(25)
    p1:Point = Point(r * math.cos(centralAngle + earSpreadAngle), r * math.sin(centralAngle + earSpreadAngle))
    p2:Point = Point(r * math.cos(centralAngle - earSpreadAngle), r * math.sin(centralAngle - earSpreadAngle))
    ear:Polygon = Polygon(p1, tip, p2)
    ear.setFill(color)
    ear.setOutline(color)
    return ear

def makeCat() -> List[GraphicsObject]:
    radius:float = 0.2
    cat: List[GraphicsObject] = []
    catColor:str = 'orange'

    cat.append(makeHead(radius, catColor))

    # Ears
    for i in range(2):
        centralAngle:float = math.radians(60) + i * math.radians(60)
        cat.append(makeCatEar(centralAngle, radius, catColor))

    cat.extend(makeEyeList(radius, 'green'))
    cat.extend(makeMouth(radius))
    cat.extend(makeWhiskerList(radius))

    return cat

def getLocation(animal:List[GraphicsObject]) -> Point:
    # Pre: animal[0] has a getCenter() method
    assert type(animal[0]) in [Circle, Line, Oval, Rectangle]
    return animal[0].getCenter()

# Function has the side effect of moving the animal to dest
def moveTo(dest:Point, animal:List[GraphicsObject]) -> None:
    # Pre: animal[0] has to have a getCenter() method
    assert type(animal[0]) in [Circle, Line, Oval, Rectangle]

    # Center of the head, which is item 0 on the list
    currentPos:Point = getLocation(animal)
    dx:float = dest.getX() - currentPos.getX()
    dy:float = dest.getY() - currentPos.getY()
    # Everything's a GraphicsObject, even though they're not all the same
    for part in animal:
        part.move(dx, dy)
    # Post: all the parts of the animal moved (side effect) AND
    assert math.isclose(animal[0].getCenter().getX(), dest.getX()) and \
        math.isclose(animal[0].getCenter().getY(), dest.getY())

def drawAnimal(win:GraphWin, animal:List[GraphicsObject]) -> None:
    # Pre: None of the parts on the animal list are drawn
    for part in animal:
        part.draw(win)
    # Post: All of the objects on the animal list are drawn (side effect)

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)
    win.setCoords(-1, -1, 1, 1)

    # Create a "mouse" to chase the mouse clicks
    mouse:List[GraphicsObject] = makeMouse()
    cat:List[GraphicsObject] = makeCat()

    # Initially off the screen
    moveTo(Point(2, 0), mouse)
    moveTo(Point(4, 0), cat)

    drawAnimal(win, mouse)
    drawAnimal(win, cat)
    
    quitButton:Rectangle = makeButton(Point(-1, 1), Point(-.5, .5),
                            'Quit', win)
    
    p:Point = win.getMouse()
    while not inButton(p, quitButton):
        moveTo(getLocation(mouse), cat)
        moveTo(p, mouse)
        p = win.getMouse()  # Update the mouse click!!

    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)