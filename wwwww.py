import keyboard
import sys
import time

def print_loading_bar(progress):
    sys.stdout.write(f"\r[{progress}{'-' * (10 - len(progress))}]")
    sys.stdout.flush()

def main():
    print("Press 'Left Arrow' to stop the loading bars.")

    for i in range(1, 6):
        loading_progress = '#' * i
        print_loading_bar(loading_progress)

        # Check for Left Arrow key press
        if keyboard.is_pressed('left'):
            break

        # Sleep for 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()
