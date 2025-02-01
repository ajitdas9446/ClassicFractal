import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
width, height = 800, 800

# Triangle vertices
vertices = [
    [-0.5, -0.5],  # Bottom-left
    [0.5, -0.5],   # Bottom-right
    [0.0, 0.5]     # Top
]

# Global variables for animation
current_depth = 0  # Current recursion depth
max_depth = 5      # Maximum recursion depth
delay = 1.0        # Delay between steps (in seconds)

def draw_triangle(p1, p2, p3, depth):
    """
    Draw a triangle given three vertices and a depth level.
    """
    # Set color based on depth
    colors = [
        (1.0, 0.0, 0.0),  # Red
        (0.0, 1.0, 0.0),  # Green
        (0.0, 0.0, 1.0),  # Blue
        (1.0, 1.0, 0.0),  # Yellow
        (1.0, 0.0, 1.0),  # Magenta
        (0.0, 1.0, 1.0)   # Cyan
    ]
    glColor3f(*colors[depth % len(colors)])  # Cycle through colors

    # Draw the triangle
    glBegin(GL_TRIANGLES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glVertex2f(p3[0], p3[1])
    glEnd()

def sierpinski(p1, p2, p3, depth):
    """
    Recursively draw the Sierpinski triangle.
    """
    if depth == 0:
        draw_triangle(p1, p2, p3, current_depth)
    else:
        # Calculate midpoints of each side
        mid1 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        mid2 = [(p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2]
        mid3 = [(p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2]

        # Recursively draw smaller triangles
        sierpinski(p1, mid1, mid3, depth - 1)
        sierpinski(mid1, p2, mid2, depth - 1)
        sierpinski(mid3, mid2, p3, depth - 1)

def display():
    """
    Display callback function.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Default color (black, but overridden in draw_triangle)

    # Draw the Sierpinski triangle up to the current depth
    sierpinski(vertices[0], vertices[1], vertices[2], current_depth)

    glFlush()

def reshape(w, h):
    """
    Reshape callback function.
    """
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set coordinate system
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def update(value):
    """
    Timer callback function to update the animation.
    """
    global current_depth
    if current_depth < max_depth:
        current_depth += 1
        glutPostRedisplay()  # Trigger redraw
        glutTimerFunc(int(delay * 1000), update, 0)  # Call update again after delay

def main():
    """
    Main function to initialize and run the program.
    """
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Sierpinski Triangle")

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    # Start the animation
    glutTimerFunc(int(delay * 1000), update, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
# # Sierpinksi generation

# import sys
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# # Window dimensions
# width, height = 800, 800

# # Initial triangle vertices for the Sierpinski Gasket
# vertices = [
#     (-0.8, -0.8),  # Bottom-left corner
#     (0.8, -0.8),   # Bottom-right corner
#     (0.0, 0.8)     # Top corner
# ]

# # Number of points to generate
# num_points = 5000

# def draw_sierpinski():
#     """
#     Draws the Sierpinski Gasket by iteratively plotting points inside a triangle.
#     """
#     glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

#     # Pick a random initial point inside the triangle
#     x, y = random.uniform(-0.8, 0.8), random.uniform(-0.8, 0.8)

#     glBegin(GL_POINTS)

#     for _ in range(num_points):
#         # Randomly choose one of the triangle's vertices
#         vx, vy = random.choice(vertices)

#         # Move halfway towards the chosen vertex
#         x = (x + vx) / 2.0
#         y = (y + vy) / 2.0

#         # Plot the point
#         glVertex2f(x, y)

#     glEnd()
#     glFlush()

# def reshape(w, h):
#     """
#     Adjusts the viewport and projection matrix when the window is resized.
#     :param w: New width of the window.
#     :param h: New height of the window.
#     """
#     glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
#     glMatrixMode(GL_PROJECTION)  # Select the projection matrix
#     glLoadIdentity()  # Reset the projection matrix
#     gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set an orthographic projection matching the window dimensions
#     glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
#     glLoadIdentity()  # Reset the model-view matrix

# def main():
#     """
#     Initializes the GLUT environment and runs the Sierpinski Gasket visualization.
#     """
#     glutInit(sys.argv)  # Initialize the GLUT library
#     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
#     glutInitWindowSize(width, height)  # Set the initial window size
#     glutCreateWindow(b"Sierpinski Gasket")  # Create the window with a title

#     glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
#     glColor3f(0.0, 0.0, 0.0)  # Set the point color to black
#     glutDisplayFunc(draw_sierpinski)  # Register the display callback function
#     glutReshapeFunc(reshape)  # Register the reshape callback function

#     glutMainLoop()  # Enter the GLUT event-processing loop

# if __name__ == "__main__":
#     main()
