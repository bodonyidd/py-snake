import tkinter as tk
from threading import Thread, Event
import time

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar Demo")
        self.root.geometry("300x100")

        self.canvas = tk.Canvas(self.root, width=200, height=20, borderwidth=1, relief="solid")
        self.canvas.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_progress)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_progress)
        self.stop_button.pack(side="left", padx=10)

        self.progress_thread = None

    def start_progress(self):
        self.canvas.delete("progress_rect")
        self.event=Event()
        # self.my_thread = MyThread(target=self.update_progress)
        # self.my_thread.start()

        # Optionally, you can wait for the thread to finish gracefully
        self.progress_thread = Thread(target=self.update_progress)
        self.progress_thread.start()

    def update_progress(self):
        for i in range(101):
            time.sleep(0.1)
            self.draw_progress_bar(i)

    def draw_progress_bar(self, percentage):
        self.canvas.delete("progress_rect")
        bar_width = 200
        bar_height = 20
        fill_width = bar_width * (percentage / 100.0)
        self.canvas.create_rectangle(0, 0, fill_width, bar_height, fill="blue", outline="")
        self.canvas.update_idletasks()

    def stop_progress(self):
        # if self.progress_thread and self.progress_thread.is_alive():
            self.event.set()
            self.progress_thread.join()
            if self.event.is_set():
                return
# ##################
            

    

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
