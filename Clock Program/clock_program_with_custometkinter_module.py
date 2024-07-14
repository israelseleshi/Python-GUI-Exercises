from customtkinter import *
from time import *

def update():

  time_string = strftime('%I:%M:%S %p')
  time_label.configure(text = time_string)

  date_string = strftime('%A, %B %d, %Y')
  date_label.configure(text = date_string)

  window.after(1000, update)


def centerWindow(window, width, height):

  screenWidth = window.winfo_screenwidth()
  screenHeight = window.winfo_screenheight()

  x = ( screenWidth // 2 ) - ( width // 2)
  y = ( screenHeight // 2 ) - ( height // 2 )

  window.geometry(f'{width}x{height}+{x}+{y}')

window = CTk()
centerWindow(window, 350, 160)

time_label = CTkLabel(window,
                      font = ("Poppins", 50),
                      text_color = "#D8F0F5"
                      )
time_label.pack(padx = 20, pady = 10)


date_label = CTkLabel(window,
                      font = ("Poppins", 25),
                      text_color = "#D8F0F5"
                      )
date_label.pack(padx = 20)

update()

window.mainloop()