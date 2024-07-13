import customtkinter as ctk
from login_window import LoginPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.switch_frame(LoginPage(self))

    def switch_frame(self, frame):
        new_frame = frame
        if hasattr(self, "_current_frame"):
            self._current_frame.destroy()
        self._current_frame = new_frame
        self._current_frame.pack(expand=True, fill="both")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
