import keyboard
import time

def loading_bar():
    while True:
        if keyboard.is_pressed(' '):
            for i in range(101):
                print('\rLoading: [{}{}] {}%'.format('=' * (i // 5), ' ' * ((100 - i) // 5), i), end='', flush=True)
                time.sleep(0.05)

                if keyboard.is_pressed('enter'):
                    print('\nLoading canceled.')
                    return

            print('\nLoading complete!')
            print('\nPress space to start again or enter to exit.')
            keyboard.wait('space')
        else:
            time.sleep(0.1)

if __name__ == "__main__":
    print("Press space to start the loading bar. Press enter to exit.")
    loading_bar()
    # print((56 / 5))  # 11.2
    # print((56 // 5)) # 11
    
