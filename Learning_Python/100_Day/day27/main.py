from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=600, height=300)

#label


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # to show label in window
# update label
my_label.config(text="New Text")



#Button

# function for button
def button_clicked():
    print("I got clicked")
    
    # get from input field
    new_text = input.get()
    
    # change the text
    my_label.config(text=new_text)
    

#create buttons
button = Button(text="Click me", command=button_clicked)
button.pack()



#Entry

# make input field
input = Entry(width=10)
input.pack()

# get something from input field
#input.get()


window.mainloop()