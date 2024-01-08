import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady= 200)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# my_label.config(padx=20, pady=20)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")


# button
def button_clicked():
    # my_label["text"] = "Button got clicked"
    my_label["text"] = input.get()
    print("I got clicked")


button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#New Button
new_button = tkinter.Button(text="New Button")
new_button.grid(column = 2, row=0)


#Entry
input = tkinter.Entry(width=15)
# input.pack()
print(input.get())
input.grid(column=4,row=4)

window.mainloop()
