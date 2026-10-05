import turtle
import math

# Window setup
screen = turtle.Screen()
screen.title("Beating Heart")
screen.bgcolor("black")
screen.setup(width=800, height=700)

# Turn off automatic drawing updates for smooth animation
screen.tracer(0)

heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)

# Change this to make the heart longer/taller.
VERTICAL_STRETCH = 1.35

# Change this to make the overall heart bigger or smaller.
BASE_SIZE = 14


def draw_heart(scale):
    """Draw one filled heart at the current beat size."""
    heart.clear()
    heart.penup()

    points = []

    # Create points from the parametric heart formula.
    for i in range(361):
        t = math.radians(i)

        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        x *= BASE_SIZE * scale
        y *= BASE_SIZE * VERTICAL_STRETCH * scale

        points.append((x, y))

    # Move to first heart point.
    heart.goto(points[0])
    heart.pendown()

    # Draw and fill the heart.
    heart.color("#ff1744", "#e6002d")
    heart.begin_fill()

    for x, y in points[1:]:
        heart.goto(x, y)

    heart.goto(points[0])
    heart.end_fill()
    heart.penup()

    # Add a small shine to make it look less flat.
    heart.goto(-45 * scale, 95 * VERTICAL_STRETCH * scale)
    heart.dot(18 * scale, "#ff8a9b")


start_time = screen.getcanvas().winfo_toplevel().tk.call("clock", "milliseconds") / 1000


def animate():
    now = screen.getcanvas().winfo_toplevel().tk.call("clock", "milliseconds") / 1000
    elapsed = now - start_time

    # A "lub-dub" heartbeat: one larger beat, then a smaller one.
    beat = (
        math.exp(-((elapsed % 1.2 - 0.12) / 0.08) ** 2)
        + 0.55 * math.exp(-((elapsed % 1.2 - 0.34) / 0.10) ** 2)
    )

    # Heart becomes larger briefly during each beat.
    scale = 1.0 + 0.14 * beat

    draw_heart(scale)
    screen.update()

    # Run the next animation frame in about 30 milliseconds.
    screen.ontimer(animate, 30)


animate()
turtle.done()