# Sierpinksi generation

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
width, height = 800, 800

# Initial triangle vertices for the Sierpinski Gasket
vertices = [
    (-0.8, -0.8),  # Bottom-left corner
    (0.8, -0.8),   # Bottom-right corner
    (0.0, 0.8)     # Top corner
]

# Number of points to generate
num_points = 5000

def draw_sierpinski():
    """
    Draws the Sierpinski Gasket by iteratively plotting points inside a triangle.
    """
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    # Pick a random initial point inside the triangle
    x, y = random.uniform(-0.8, 0.8), random.uniform(-0.8, 0.8)

    glBegin(GL_POINTS)

    for _ in range(num_points):
        # Randomly choose one of the triangle's vertices
        vx, vy = random.choice(vertices)

        # Move halfway towards the chosen vertex
        x = (x + vx) / 2.0
        y = (y + vy) / 2.0

        # Plot the point
        glVertex2f(x, y)

    glEnd()
    glFlush()

def reshape(w, h):
    """
    Adjusts the viewport and projection matrix when the window is resized.
    :param w: New width of the window.
    :param h: New height of the window.
    """
    glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
    glMatrixMode(GL_PROJECTION)  # Select the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set an orthographic projection matching the window dimensions
    glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
    glLoadIdentity()  # Reset the model-view matrix

def main():
    """
    Initializes the GLUT environment and runs the Sierpinski Gasket visualization.
    """
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
    glutInitWindowSize(width, height)  # Set the initial window size
    glutCreateWindow(b"Sierpinski Gasket")  # Create the window with a title

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glColor3f(0.0, 0.0, 0.0)  # Set the point color to black
    glutDisplayFunc(draw_sierpinski)  # Register the display callback function
    glutReshapeFunc(reshape)  # Register the reshape callback function

    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()
