import keyboard

def main():
    print("Press 'esc' to exit.")
    while True:
        key_event = keyboard.read_event(suppress=True)
        if key_event.event_type == keyboard.KEY_DOWN:
            key = key_event.name
            print(f"Key pressed: {key}")
            if key == 'esc':
                break

if __name__ == "__main__":
    main()
