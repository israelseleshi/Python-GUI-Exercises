from tkinter import *

def center_window(window, width, height):

  # Get screen width and height
  screen_width = window.winfo_screenwidth()
  screen_height = window.winfo_screenheight()

  # Calculate position x, t
  x = ( screen_width // 2 ) - (width // 2)
  y = ( screen_height // 2) - (height // 2)

  window.geometry(f"{width}x{height}+{x}+{y}")

class CounterApp:
 

  def __init__(self, root):
    self.root = root
    self.root.title("Simple Counter")
    center_window(self.root, 400, 200)

    self.count = 0

    self.label = Label(root,
                       text = "Count: 0",
                       font = ("Helvetica", 16)
                       )
    self.label.pack(pady = 10)

    self.increase_button = Button(root,
                         text = "Increase Count",
                         command = self.increase_count,
                         font = ("Helvetica", 12)
                         ) 
    self.increase_button.pack(pady = 10)
    
    self.decrease_button = Button(root,
                         text = "Decrease Count",
                         command = self.decrease_count,
                         font = ("Helvetica", 12)
                         ) 
    self.decrease_button.pack(pady = 10)

    self.reset_button = Button(root,
                         text = "Reset Count",
                         command = self.reset_count,
                         font = ("Helvetica", 12)
                         ) 
    self.reset_button.pack(pady = 10)

  def increase_count(self):
    self.count += 1
    self.label.configure(text = f"Count: {self.count}")
  
  def decrease_count(self):
    self.count -= 1
    self.label.configure(text = f"Count: {self.count}")

  def reset_count(self):
    self.count = 0
    self.label.configure(text = f"Count: {self.count}")

if __name__ == "__main__":
  root = Tk()
  app = CounterApp(root)
  root.mainloop()