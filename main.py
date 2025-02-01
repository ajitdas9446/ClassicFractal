import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import subprocess

# Menu options
menu_text = [
    "Choose a Fractal Generation:",
    "1. Mandelbrot Set",
    "2. Snowflake (Koch Curve)",
    "3. Tree",
    "4. Sierpinski Triangle",
    "5. Christmas Tree",
    "0. Quit"
]

# Window dimensions
width, height = 800, 600

# Function to render text
def render_text(text, x, y):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))  # type: ignore

# Function to display the menu
def display_menu():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    glColor3f(1.0, 1.0, 1.0)  # Set text color to white

    # Render menu text
    y_offset = 0.9
    for line in menu_text:
        render_text(line, -0.9, y_offset)
        y_offset -= 0.1

    glFlush()  # Ensure all drawing commands are executed
    glutSwapBuffers()  # Swap buffers for double buffering

# Function to handle keyboard input
def on_key_press(key, x, y):
    choice = key.decode()  # Decode the pressed key
    if choice in "012345":  # Check if the key corresponds to a valid option
        print(f"Selected option: {choice}")
        run_fractal(int(choice))

# Function to run the selected fractal script
def run_fractal(choice):
    try:
        scripts = ["a.py", "b.py", "c.py", "d.py", "e.py"]
        if 1 <= choice <= 5:
            subprocess.run(["python3", scripts[choice - 1]])  # Run corresponding script
        elif choice == 0:
            print("Exiting...")
            sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")

# Function to handle the window resizing event
def reshape(w, h):
    glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
    glMatrixMode(GL_PROJECTION)  # Select the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set an orthographic projection
    glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
    glLoadIdentity()  # Reset the model-view matrix

# Main function to initialize OpenGL
def main():
    glutInit(sys.argv)  # Initialize the GLUT library
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering and RGB color mode
    glutInitWindowSize(width, height)  # Set the initial window size
    glutCreateWindow(b"Fractal Selection Menu")  # Create the window with a title

    # Set up OpenGL settings
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the background color to black

    # Register callback functions
    glutDisplayFunc(display_menu)  # Register the display callback function
    glutReshapeFunc(reshape)  # Register the reshape callback function
    glutKeyboardFunc(on_key_press)  # Register the keyboard input callback function

    # Enter the GLUT event-processing loop
    glutMainLoop()

if __name__ == "__main__":
    main()

# import sys
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import subprocess

# # Fractal selection menu text
# menu_text = [
#     "Choose a Fractal Generation:",
#     "1. Mandelbrot Set",
#     "2. Snowflake (Koch Curve)",
#     "3. Tree",
#     "4. Sierpinski Triangle",
#     "5. Christmas Tree",
#     "0. Quit"
# ]

# # Window dimensions
# width, height = 800, 600

# # Current selected option
# selected_option = None

# # Function to render text on the OpenGL screen
# def render_text(text, x, y):
#     glRasterPos2f(x, y)
#     for char in text:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char)) # type: ignore

# # Function to display the menu
# def display_menu():
#     glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
#     glColor3f(1.0, 1.0, 1.0)  # Set text color to white

#     # Render menu text
#     y_offset = 0.9
#     for line in menu_text:
#         render_text(line, -0.9, y_offset)
#         y_offset -= 0.1

#     glFlush()  # Ensure all drawing commands are executed
#     glutSwapBuffers()  # Swap buffers for double buffering

# # Function to handle mouse click events
# def on_mouse_click(button, state, x, y):
#     global selected_option

#     # Map screen coordinates to OpenGL coordinates
#     y = height - y  # Convert to OpenGL y-coordinate system

#     # Check if the click is within a specific menu option
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         if 600 > y > 540:  # 1st option
#             selected_option = 1
#         elif 540 > y > 480:  # 2nd option
#             selected_option = 2
#         elif 480 > y > 420:  # 3rd option
#             selected_option = 3
#         elif 420 > y > 360:  # 4th option
#             selected_option = 4
#         elif 360 > y > 300:  # 5th option
#             selected_option = 5
#         elif 300 > y > 240:  # 0th option (Quit)
#             selected_option = 0

#         if selected_option != None:
#             print(f"Selected option: {selected_option}")
#             run_fractal(selected_option)

# # Function to run the selected fractal script
# def run_fractal(choice):
#     try:
#         if choice == 1:
#             subprocess.run(["python3", "a.py"])  # Run a.py (Mandelbrot)
#         elif choice == 2:
#             subprocess.run(["python3", "b.py"])  # Run b.py (Snowflake)
#         elif choice == 3:
#             subprocess.run(["python3", "c.py"])  # Run c.py (Tree)
#         elif choice == 4:
#             subprocess.run(["python3", "d.py"])  # Run d.py (Sierpinski)
#         elif choice == 5:
#             subprocess.run(["python3", "e.py"])  # Run e.py (Christmas Tree)
#         elif choice == 0:
#             print("Exiting...")
#             sys.exit(0)
#     except Exception as e:
#         print(f"Error: {e}")

# # Function to handle the window resizing event
# def reshape(w, h):
#     glViewport(0, 0, w, h)  # Set the viewport to cover the entire window
#     glMatrixMode(GL_PROJECTION)  # Select the projection matrix
#     glLoadIdentity()  # Reset the projection matrix
#     gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set an orthographic projection
#     glMatrixMode(GL_MODELVIEW)  # Select the model-view matrix
#     glLoadIdentity()  # Reset the model-view matrix

# # Main function to initialize OpenGL
# def main():
#     glutInit(sys.argv)  # Initialize the GLUT library
#     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering and RGB color mode
#     glutInitWindowSize(width, height)  # Set the initial window size
#     glutCreateWindow(b"Fractal Selection Menu")  # Create the window with a title

#     # Set up OpenGL settings
#     glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the background color to black
#     glColor3f(1.0, 1.0, 1.0)  # Set the text color to white

#     # Register callback functions
#     glutDisplayFunc(display_menu)  # Register the display callback function
#     glutReshapeFunc(reshape)  # Register the reshape callback function
#     glutMouseFunc(on_mouse_click)  # Register the mouse click callback function

#     # Enter the GLUT event-processing loop
#     glutMainLoop()

# if __name__ == "__main__":
#     main()

# # import sys
# # import subprocess

# # def display_menu():
# #     """
# #     Display the menu with choices in the terminal.
# #     """
# #     print("\nChoose a Fractal Generation:")
# #     print("1. Mandelbrot Set")
# #     print("2. Snowflake (Koch Curve)")
# #     print("3. Tree")
# #     print("4. Sierpinski Triangle")
# #     print("5. Christmas Tree")
# #     print("0. Quit")
# #     print("\nPress corresponding number to select:")

# # def main():
# #     """
# #     Main function to run the terminal-based menu for fractal generation.
# #     """
# #     while True:
# #         display_menu()  # Display the menu
        
# #         try:
# #             choice = int(input("Enter your choice: "))  # Take input from user
            
# #             if choice == 0:
# #                 print("Exiting the program.")
# #                 sys.exit()  # Exit the program

# #             elif choice == 1:
# #                 print("Running Mandelbrot Set (a.py)...")
# #                 subprocess.run(["python3", "a.py"])  # Run a.py as a separate process

# #             elif choice == 2:
# #                 print("Running Snowflake (Koch Curve) (b.py)...")
# #                 subprocess.run(["python3", "b.py"])  # Run b.py as a separate process

# #             elif choice == 3:
# #                 print("Running Tree generation (c.py)...")
# #                 subprocess.run(["python3", "c.py"])  # Run c.py as a separate process

# #             elif choice == 4:
# #                 print("Running Sierpinski Triangle (d.py)...")
# #                 subprocess.run(["python3", "d.py"])  # Run d.py as a separate process

# #             elif choice == 5:
# #                 print("Running Christmas Tree (e.py)...")
# #                 subprocess.run(["python3", "e.py"])  # Run e.py as a separate process

# #             else:
# #                 print("Invalid choice! Please select a number between 0 and 5.")
        
# #         except ValueError:
# #             print("Invalid input! Please enter a number between 0 and 5.")
# #         except Exception as e:
# #             print(f"Error occurred: {e}")
# #             # Capture the traceback for better debugging
# #             import traceback
# #             traceback.print_exc()

# # if __name__ == "__main__":
# #     main()
