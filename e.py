# twin christmas tree generation

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

# Window dimensions
width, height = 800, 800

# Parameters for twin Christmas trees
initial_length = 0.4  # Length of the initial branches (reduced to fit in the window)
recursion_depth = 8   # Number of recursive levels
branch_angle = math.pi / 6  # Angle between branches

# Scaling factor for the entire tree
scale_factor = 0.5  # Reduce the tree size

# Store the drawing steps to simulate the animation
drawing_steps = []

def draw_branch(x, y, length, angle, depth, direction):
    """
    Recursively draws branches for a Christmas tree and stores the steps for animation.
    :param x: Starting x-coordinate of the branch.
    :param y: Starting y-coordinate of the branch.
    :param length: Length of the current branch.
    :param angle: Angle of the current branch.
    :param depth: Current recursion depth.
    :param direction: -1 for left tree, +1 for right tree.
    """
    if depth == 0:
        return

    # Calculate the end coordinates of the branch
    x_end = x + length * math.cos(angle)
    y_end = y + length * math.sin(angle)

    # Store the drawing step (start and end points of the branch)
    drawing_steps.append((x, y, x_end, y_end))

    # Reduce branch length and recurse
    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + branch_angle * direction, depth - 1, direction)
    draw_branch(x_end, y_end, new_length, angle - branch_angle * direction, depth - 1, direction)

def draw_twin_trees():
    """
    Draws two symmetrical Christmas trees with animation.
    """
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    
    # Draw the left tree (scaled and shifted to fit in the window)
    draw_branch(-0.5 * scale_factor, -0.8 * scale_factor, initial_length * scale_factor, math.pi / 2, recursion_depth, direction=-1)

    # Draw the right tree (scaled and shifted to fit in the window)
    draw_branch(0.5 * scale_factor, -0.8 * scale_factor, initial_length * scale_factor, math.pi / 2, recursion_depth, direction=1)

    glFlush()  # Ensure all drawing commands are executed

def display():
    """
    Update the display with one step of the drawing process.
    """
    if len(drawing_steps) > 0:
        # Get the next step to draw
        x1, y1, x2, y2 = drawing_steps.pop(0)

        # Draw the current branch
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glFlush()  # Ensure the branch is drawn immediately

    # Continue drawing if there are more steps left
    if len(drawing_steps) > 0:
        glutPostRedisplay()  # Request the next display update
    else:
        time.sleep(1)  # Wait for a second before finishing the animation

def reshape(w, h):
    """
    Adjusts the viewport and projection matrix when the window is resized.
    :param w: New width of the window.
    :param h: New height of the window.
    """
    glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
    glMatrixMode(GL_PROJECTION)  # Select the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)  # Set an orthographic projection with extended range
    glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
    glLoadIdentity()  # Reset the model-view matrix

def main():
    """
    Initializes the GLUT environment and runs the twin Christmas trees visualization.
    """
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
    glutInitWindowSize(width, height)  # Set the initial window size
    glutCreateWindow(b"Twin Christmas Trees")  # Create the window with a title

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glColor3f(0.0, 0.8, 0.0)  # Set the tree color to green
    glutDisplayFunc(display)  # Register the display callback function
    glutReshapeFunc(reshape)  # Register the reshape callback function

    # Start drawing the trees to populate the drawing steps
    draw_twin_trees()

    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()
