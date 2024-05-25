from tkinter import *

def button_clicked():
    print('I got clicked')
    my_label['text'] = input.get()   #getting text which is printed by the use in the window


window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.config(text='New text')
my_label.grid(column=0, row=0)

#Button
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

#Button2
new_button = Button(text='Click Me2', command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10,)
print(input.get())
input.grid(column=3, row=3)







window.mainloop()