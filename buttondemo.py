from graphics import *
from typing import List

def makeButton(p1:Point, p2:Point, text:str, w:GraphWin) -> Rectangle:
    button:Rectangle = Rectangle(p1, p2)
    label:Text = Text(button.getCenter(), text)
    button.draw(w)
    label.draw(w)
    return button

def inButton(click:Point, button:Rectangle) -> bool:
    p1:Point = button.getP1()
    p2:Point = button.getP2()
    minX:float = min(p1.getX(), p2.getX())
    maxX:float = max(p1.getX(), p2.getX())
    minY:float = min(p1.getY(), p2.getY())
    maxY:float = max(p1.getY(), p2.getY())

    return minX <= click.getX() <= maxX and \
            minY <= click.getY() <= maxY

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    button:Rectangle = makeButton(Point(-.5, .5), Point(0.5, -0.5),
                                    'Click here', win)
    for i in range(5):
        click = win.getMouse()
        if inButton(click, button):
            print('Inside')
        else:
            print('Outside')


    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)