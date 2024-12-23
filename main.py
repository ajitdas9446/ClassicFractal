import sys
import subprocess

def display_menu():
    """
    Display the menu with choices in the terminal.
    """
    print("\nChoose a Fractal Generation:")
    print("1. Mandelbrot Set")
    print("2. Snowflake (Koch Curve)")
    print("3. Tree")
    print("4. Sierpinski Triangle")
    print("5. Christmas Tree")
    print("0. Quit")
    print("\nPress corresponding number to select:")

def main():
    """
    Main function to run the terminal-based menu for fractal generation.
    """
    while True:
        display_menu()  # Display the menu
        
        try:
            choice = int(input("Enter your choice: "))  # Take input from user
            
            if choice == 0:
                print("Exiting the program.")
                sys.exit()  # Exit the program

            elif choice == 1:
                print("Running Mandelbrot Set (a.py)...")
                subprocess.run(["python3", "a.py"])  # Run a.py as a separate process

            elif choice == 2:
                print("Running Snowflake (Koch Curve) (b.py)...")
                subprocess.run(["python3", "b.py"])  # Run b.py as a separate process

            elif choice == 3:
                print("Running Tree generation (c.py)...")
                subprocess.run(["python3", "c.py"])  # Run c.py as a separate process

            elif choice == 4:
                print("Running Sierpinski Triangle (d.py)...")
                subprocess.run(["python3", "d.py"])  # Run d.py as a separate process

            elif choice == 5:
                print("Running Christmas Tree (e.py)...")
                subprocess.run(["python3", "e.py"])  # Run e.py as a separate process

            else:
                print("Invalid choice! Please select a number between 0 and 5.")
        
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 5.")
        except Exception as e:
            print(f"Error occurred: {e}")
            # Capture the traceback for better debugging
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
