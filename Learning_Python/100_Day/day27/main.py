import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=600, height=300)

#label
my_Label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_Label.pack() # to show label in window







window.mainloop()