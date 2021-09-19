from tkinter import *


def miles_to_km():
    miles = et_mile.get()
    km = round(float(miles) * 1.609)
    show_output_label.config(text=f"{km}")


# Create a Screen
window = Tk()
window.title("Mile To Kilometer Convertor")
window.minsize(width=100, height=70)
window.config(padx=40,pady=40)


# EditText OR Entry
et_mile = Entry(width=7)
et_mile.grid(row=0, column=1)


# Labels
mile_label = Label(text="Mile")
mile_label.grid(row=0, column=2)

equal_label = Label(text="iS Equal To")
equal_label.grid(row=1, column=0)

show_output_label = Label(text="0")
show_output_label.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1,column=2)


# Button
btn_calculate = Button(text="Calculate", command=miles_to_km)
btn_calculate.grid(row=2, column=1)






window.mainloop()