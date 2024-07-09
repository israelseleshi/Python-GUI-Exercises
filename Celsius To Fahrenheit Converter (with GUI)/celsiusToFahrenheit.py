from customtkinter import *

def convertTemp():

  temp = float(enterTemp.get())
  result = float((temp * (9/5)) + 32)

  resultLabel.configure(app, text= f"{temp} C is {result} in F.")

app = CTk()
app.geometry('500x300')
app.title('Celsius To Fahrenheit Converter')

title = CTkLabel(app, text = "Celsius To Fahrenheit Converter", font = ("Consolas", 25, 'bold'))
title.grid(row = 0, column = 0, pady = 20, columnspan = 2)

enterTemp = CTkEntry(app, placeholder_text = "Enter temperature in C...", font = ("Consolas", 20, 'bold'), width = 300)
enterTemp.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew')

convertButton = CTkButton(app, text= "Convert", command = convertTemp, font = ("Consolas", 20, 'bold'))
convertButton.grid(row = 1, column = 1, padx = 10, pady = 10, sticky= 'nsew')

resultLabel = CTkLabel(app, text = "", font = ("Consolas", 25, 'bold'))
resultLabel.grid(row = 2, columnspan = 2, pady = 30, sticky = 'nsew')




app.mainloop()