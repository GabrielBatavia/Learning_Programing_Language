from tkinter import *

# function to convert
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    kilometers_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=30, pady=20)

miles_input = Entry(width=4)
miles_input.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=3, row=1)

kilometers_result_label = Label(text="0", width=3)
kilometers_result_label.grid(column=4, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=5, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=3, row=2)




window.mainloop()