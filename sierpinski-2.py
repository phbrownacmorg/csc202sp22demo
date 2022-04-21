from typing import cast, List, Tuple
import math
import turtle
from turtle import Turtle

def draw_tri(side: float, color: str, t: Turtle) -> None:
    """Draw a filled triangle of color COLOR and side SIDE, with vertices PTS,
    using Turtle T.  For an upward-pointing triangle, the pen begins and ends at
    the lower-left corner, facing right, with the pen up."""
    t.fillcolor(color)
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.up()

def midpt(p0: Tuple[float, float], p1: Tuple[float, float]) -> Tuple[float, float]:
    """Find and return the midpoint of the given points P0 and P1."""
    return ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)

def draw_sierpinski(side: float, depth: int, t: Turtle) -> None:
    """Draw a Sierpinski triangle with side SIDE and depth DEPTH,
        using Turtle T.  The turtle begins and ends at the lower-left
        corner of the triangle, facing right, with the pen up."""
    colors: List[str] = ['red', 'green', 'blue', 'white',
                         'magenta', 'yellow', 'cyan', 'black', 
                         'orange']
    # Pre:
    assert depth < len(colors)
    draw_tri(side, colors[depth], t) # Base case (also done in the recursive case)
    if depth > 0:
        draw_sierpinski(side/2, depth - 1, t)
        t.forward(side/2)
        draw_sierpinski(side/2, depth - 1, t)
        t.left(120)
        t.forward(side/2)
        t.right(120)
        draw_sierpinski(side/2, depth - 1, t)
        t.right(120)
        t.forward(side/2)
        t.left(120)

def initial_position(side: float, t: Turtle) -> None:
    """Moves the the turtle to the initial position so that the triangle can be centered."""
    t.up()
    t.backward(side/2)
    t.right(90)
    t.forward(side * math.sqrt(3)/6)
    t.left(90)

def main(args: List[str]) -> int:
    t: Turtle = Turtle()
    w = turtle.Screen()

    side = 600
    t.speed(0)
    initial_position(side, t)
    draw_sierpinski(side, 5, t)

    w.exitonclick()
    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)