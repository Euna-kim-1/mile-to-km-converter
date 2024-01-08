import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text =f"{km}")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label(doesn't change)
miles_label = tkinter.Label(text = "miles")
miles_label.grid(column =2, row=0)

km = tkinter.Label(text = "Km")
km.grid(column =2, row=1)

is_equal_label = tkinter.Label(text = "is equal to")
is_equal_label.grid(column =0, row=1)

km_result_label = tkinter.Label(text=0)
km_result_label.grid(column =1, row=1)



#Entry
miles_input = tkinter.Entry(width=5)
miles_input.grid(column=1,row=0)





button = tkinter.Button(text="Calculate", command = miles_to_km)
# button.pack()
button.grid(column=1,row=2)


window.mainloop()