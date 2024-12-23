import sys
import math
import time
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

# Window dimensions
width, height = 800, 800

# Parameters for twin Christmas trees
initial_length = 0.4  # Length of the initial branches
recursion_depth = 8   # Number of recursive levels
branch_angle = math.pi / 6  # Angle between branches
scale_factor = 0.5  # Reduce the tree size

# Store the drawing steps to simulate the animation
drawing_steps = []

# Background image path
background_image_path = "./image/desert.jpeg"  # Replace with your image file path


def load_texture():
    """
    Loads a texture from an image file.
    """
    img = Image.open(background_image_path)
    img_data = np.array(list(img.getdata()), np.uint8)

    # Enable texture mapping
    glEnable(GL_TEXTURE_2D)

    # Generate and bind texture
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)

    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Load the texture data
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    return tex_id


def draw_background():
    """
    Draws the background using a texture.
    """
    glBindTexture(GL_TEXTURE_2D, background_texture)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(-1.5, -1.5)  # Bottom-left

    glTexCoord2f(1.0, 0.0)
    glVertex2f(1.5, -1.5)  # Bottom-right

    glTexCoord2f(1.0, 1.0)
    glVertex2f(1.5, 1.5)  # Top-right

    glTexCoord2f(0.0, 1.0)
    glVertex2f(-1.5, 1.5)  # Top-left
    glEnd()


def draw_branch(x, y, length, angle, depth, direction):
    """
    Recursively draws branches for a Christmas tree and stores the steps for animation.
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
    draw_branch(-0.5 * scale_factor, -0.8 * scale_factor, initial_length * scale_factor, math.pi / 2, recursion_depth, direction=-1)
    draw_branch(0.5 * scale_factor, -0.8 * scale_factor, initial_length * scale_factor, math.pi / 2, recursion_depth, direction=1)


def display():
    """
    Updates the display with one step of the drawing process.
    """
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the background
    draw_background()

    if len(drawing_steps) > 0:
        # Get the next step to draw
        x1, y1, x2, y2 = drawing_steps.pop(0)

        # Draw the current branch
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glFlush()

    if len(drawing_steps) > 0:
        glutPostRedisplay()  # Request the next display update
    else:
        time.sleep(1)  # Pause for a second after finishing


def reshape(w, h):
    """
    Adjusts the viewport and projection matrix when the window is resized.
    """
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    """
    Initializes the GLUT environment and runs the twin Christmas trees visualization.
    """
    global background_texture

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Twin Christmas Trees with Background")

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.8, 0.0)

    # Load the background texture
    background_texture = load_texture()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    draw_twin_trees()
    glutMainLoop()


if __name__ == "__main__":
    main()
