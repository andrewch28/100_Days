from tkinter import *

def miles_to_km():
    miles=float(entry.get())
    km = round(miles * 1.609)
    label4.config(text=f"{km}")

#Window
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

#Labels

label1 = Label(text="is equal to", font=("Arial", 16, "italic"))
label1.grid(column=0, row=1)

label2 = Label(text="Miles", font=("Arial", 16, "italic"))
label2.grid(column=2,row=0)

label3 = Label(text="Km", font=("Arial", 16, "italic"))
label3.grid(column=2, row=1)

label4 = Label(text="0", font=("Arial", 16, "italic"))
label4.grid(column=1, row=1)


#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

#Entry
entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(column=1, row=0)


window.mainloop()