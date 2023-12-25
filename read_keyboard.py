import keyboard

def read_keyboard():
    key = ''
    while key != 'esc':
        key = keyboard.read_event(suppress=True).name
        return key
