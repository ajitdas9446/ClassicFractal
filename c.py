# tree generation

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window dimensions
width, height = 800, 800

# Parameters for fractal tree
angle = math.pi / 4  # Angle between branches
branch_length = 0.5  # Initial branch length
recursion_depth = 10  # Number of recursive levels

def draw_branch(x, y, length, angle, depth):
    """
    Recursively draws branches to create a fractal tree.
    :param x: Starting x-coordinate of the branch.
    :param y: Starting y-coordinate of the branch.
    :param length: Length of the current branch.
    :param angle: Angle of the current branch.
    :param depth: Current recursion depth.
    """
    if depth == 0:
        return

    # Calculate the end coordinates of the branch
    x_end = x + length * math.cos(angle)
    y_end = y + length * math.sin(angle)

    # Draw the branch as a line
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x_end, y_end)
    glEnd()

    # Recursively draw the left and right branches
    new_length = length * 0.67  # Reduce branch length for each level
    draw_branch(x_end, y_end, new_length, angle + math.pi / 6, depth - 1)  # Right branch
    draw_branch(x_end, y_end, new_length, angle - math.pi / 6, depth - 1)  # Left branch

def draw_tree():
    """
    Clears the screen and draws the fractal tree starting from the base.
    """
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    # Set initial position and orientation of the trunk
    start_x, start_y = 0.0, -0.8  # Bottom center of the screen
    draw_branch(start_x, start_y, branch_length, math.pi / 2, recursion_depth)  # Start with a vertical trunk

    glFlush()  # Ensure all drawing commands are executed

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
    Initializes the GLUT environment and runs the fractal tree visualization.
    """
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
    glutInitWindowSize(width, height)  # Set the initial window size
    glutCreateWindow(b"Fractal Tree")  # Create the window with a title

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glColor3f(0.0, 0.5, 0.0)  # Set the tree color to green
    glutDisplayFunc(draw_tree)  # Register the display callback function
    glutReshapeFunc(reshape)  # Register the reshape callback function

    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()
