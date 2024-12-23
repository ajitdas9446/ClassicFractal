# mandelbrot set generation
import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
width, height = 800, 800

# Mandelbrot parameters
max_iter = 256  # Maximum number of iterations to determine set membership
xmin, xmax = -2.0, 1.0  # Horizontal bounds of the Mandelbrot set
ymin, ymax = -1.5, 1.5  # Vertical bounds of the Mandelbrot set

def mandelbrot(x, y):
    """
    Determines the escape time for a given point in the complex plane.
    :param x: Real part of the complex number.
    :param y: Imaginary part of the complex number.
    :return: Iteration count before the sequence escapes (or max_iter).
    """
    c = complex(x, y)  # Complex number representing the point
    z = 0.0j  # Initial value of z (starts at the origin in the complex plane)
    for i in range(max_iter):
        if abs(z) > 2.0:  # Escape condition (outside the circle of radius 2)
            return i
        z = z * z + c  # Mandelbrot iteration formula
    return max_iter  # Return max_iter if the sequence does not escape

def generate_mandelbrot():
    """
    Generates the Mandelbrot set pixel values.
    :return: 3D numpy array representing pixel colors.
    """
    # Create ranges for x and y based on the window dimensions and set bounds
    x_range = np.linspace(xmin, xmax, width)
    y_range = np.linspace(ymin, ymax, height)

    # Initialize an empty pixel array (height x width x RGB channels)
    pixels = np.zeros((height, width, 3), dtype=np.uint8)

    # Iterate over every pixel and compute its color based on Mandelbrot membership
    for i, y in enumerate(y_range):
        for j, x in enumerate(x_range):
            color = mandelbrot(x, y)  # Compute escape time for the point
            color_value = 255 - int(color * 255 / max_iter)  # Map escape time to grayscale
            pixels[i, j] = (color_value, color_value, color_value)  # Set RGB color

    return pixels

def draw_mandelbrot():
    """
    Renders the Mandelbrot set onto the OpenGL window.
    """
    pixels = generate_mandelbrot()  # Generate Mandelbrot set pixel data

    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    glDrawPixels(width, height, GL_RGB, GL_UNSIGNED_BYTE, pixels)  # Draw the pixel data
    glFlush()  # Force execution of OpenGL commands

def reshape(w, h):
    """
    Adjusts the viewport and projection matrix when the window is resized.
    :param w: New width of the window.
    :param h: New height of the window.
    """
    glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
    glMatrixMode(GL_PROJECTION)  # Select the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(0, w, 0, h)  # Set an orthographic projection matching the window dimensions
    glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
    glLoadIdentity()  # Reset the model-view matrix

def main():
    """
    Main function to initialize and run the Mandelbrot visualization.
    """
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Use single buffering and RGB color mode
    glutInitWindowSize(width, height)  # Set the initial window size
    glutCreateWindow(b"Mandelbrot Set")  # Create the window with a title

    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the background color to black
    glutDisplayFunc(draw_mandelbrot)  # Register the display callback function
    glutReshapeFunc(reshape)  # Register the reshape callback function

    glutMainLoop()  # Enter the GLUT event-processing loop

if __name__ == "__main__":
    main()
