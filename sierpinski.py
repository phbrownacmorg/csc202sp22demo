from typing import cast, List, Tuple
import turtle
from turtle import Turtle

def draw_tri(pts: List[Tuple[float, float]], color: str, 
                t: Turtle) -> None:
    """Draw a filled triangle of color COLOR, with vertices PTS,
    using Turtle T.  The turtle is left at pts[0] with the pen down."""
    t.fillcolor(color)
    t.up()
    t.goto(pts[0][0], pts[0][1])
    t.down()
    t.begin_fill()
    t.goto(pts[1][0], pts[1][1])
    t.goto(pts[2][0], pts[2][1])
    t.goto(pts[0][0], pts[0][1])
    t.end_fill()

def midpt(p0: Tuple[float, float], p1: Tuple[float, float]) -> Tuple[float, float]:
    """Find and return the midpoint of the given points P0 and P1."""
    return ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)

def draw_sierpinski(pts: List[Tuple[float, float]], depth: int, 
                    t: Turtle) -> None:
    """Draw a Sierpinski triangle with vertices PTS and depth DEPTH,
        using Turtle T."""
    colors: List[str] = ['red', 'green', 'blue', 'white',
                         'magenta', 'yellow', 'cyan', 'black', 
                         'orange']
    # Pre:
    assert depth < len(colors)
    draw_tri(pts, colors[depth], t) # Base case (also done in the recursive case)
    if depth > 0:
        draw_sierpinski([pts[0], midpt(pts[0], pts[1]), midpt(pts[0], pts[2])],
                        depth - 1, t)
        draw_sierpinski([pts[1], midpt(pts[1], pts[2]), midpt(pts[1], pts[0])],
                        depth - 1, t)
        draw_sierpinski([pts[2], midpt(pts[2], pts[0]), midpt(pts[2], pts[1])],
                        depth - 1, t)

def main(args: List[str]) -> int:
    t: Turtle = Turtle()
    w = turtle.Screen()

    pts: List[Tuple[float, float]] = [(-180, -150), (0, 150), (180, -150)]
    draw_sierpinski(pts, 4, t)

    w.exitonclick()
    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)