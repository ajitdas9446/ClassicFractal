import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window dimensions
width, height = 800, 800

# Current recursion depth for animation
current_order = 0
max_order = 4  # Maximum recursion depth

def draw_line(p1, p2):
    """
    Draws a straight line between two points.
    :param p1: Starting point (x1, y1)
    :param p2: Ending point (x2, y2)
    """
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])

def koch_snowflake(order, p1, p2):
    """
    Recursively generates the Koch snowflake pattern.
    :param order: Current recursion depth.
    :param p1: Starting point of the segment.
    :param p2: Ending point of the segment.
    """
    if order == 0:
        # Base case: Draw a straight line
        draw_line(p1, p2)
    else:
        # Decompose the line segment into three parts
        x1, y1 = p1
        x2, y2 = p2

        # Calculate the first and second division points (p3 and p4)
        p3 = ((2 * x1 + x2) / 3, (2 * y1 + y2) / 3)
        p4 = ((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3)

        # Compute the peak of the equilateral triangle to be added (p5)
        dx, dy = x2 - x1, y2 - y1  # Direction vector of the segment
        angle = math.pi / 3  # 60 degrees in radians
        px = p3[0] + math.cos(angle) * dx / 3 - math.sin(angle) * dy / 3
        py = p3[1] + math.sin(angle) * dx / 3 + math.cos(angle) * dy / 3
        p5 = (px, py)

        # Recursively apply the Koch pattern to the four new segments
        koch_snowflake(order - 1, p1, p3)
        koch_snowflake(order - 1, p3, p5)
        koch_snowflake(order - 1, p5, p4)
        koch_snowflake(order - 1, p4, p2)

def draw_snowflake():
    """
    Clears the screen and draws the Koch snowflake up to the current recursion depth.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)  # Start drawing lines

    # Define the initial vertices of the triangle
    p1 = (-0.5, -0.3)
    p2 = (0.5, -0.3)
    p3 = (0.0, 0.6)

    # Draw each side of the triangle with the Koch snowflake pattern
    koch_snowflake(current_order, p1, p2)
    koch_snowflake(current_order, p2, p3)
    koch_snowflake(current_order, p3, p1)

    glEnd()  # End drawing lines
    glFlush()  # Ensure all drawing commands are executed

def animate(value):
    """
    Timer callback function to incrementally draw the Koch snowflake.
    :param value: Timer value (not used here).
    """
    global current_order

    if current_order < max_order:
        current_order += 1  # Increment the recursion depth
        glutPostRedisplay()  # Request to redraw the screen
        glutTimerFunc(1000, animate, 0)  # Set the timer for the next frame

def reshape(w, h):
    """
    Handles window resizing to maintain the correct aspect ratio.
    :param w: New width of the window.
    :param h: New height of the window.
    """
    glViewport(0, 0, w, h)  # Set the viewport to cover the new window
    glMatrixMode(GL_PROJECTION)  # Select the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set an orthographic projection
    glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
    glLoadIdentity()  # Reset the model-view matrix

def main():
    """
    Initializes the GLUT environment and runs the main loop.
    """
    glutInit(sys.argv)  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode
    glutInitWindowSize(width, height)  # Set window size
    glutCreateWindow(b"Koch Snowflake Animation")  # Create the window with a title

    # Set up the rendering environment
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glColor3f(0.0, 0.0, 0.0)  # Set drawing color to black
    glutDisplayFunc(draw_snowflake)  # Register the display callback
    glutReshapeFunc(reshape)  # Register the reshape callback
    glutTimerFunc(1000, animate, 0)  # Start the animation timer (1000ms interval)

    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()
