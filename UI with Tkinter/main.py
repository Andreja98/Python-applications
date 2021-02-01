from tkinter import *

# Inicijalizujemo objekat tj prozor. Sve se dodaje izmedju inicijalizacije i mainloop() metode
window = Tk()


def miles():
    miles = float(entry_value.get()) * 1.6
    # END znaci da ce tekst uvek dodavati na kraj bloka teksta
    text.insert(END, miles)


def convert():
    kgs_to_grams = float(entry_value_user.get()) * 1000
    kg_to_pounds = float(entry_value_user.get()) * 2.20462
    kg_to_ounces = float(entry_value_user.get()) * 35.274
    text_for_grams.insert(END, kgs_to_grams)
    text_for_pounds.insert(END, kg_to_pounds)
    text_for_ounces.insert(END, kg_to_ounces)


label = Label(window, text="Kg", height=1, width=20)
label.grid(row=0, column=0)

entry_value_user = StringVar()
user_entry = Entry(window, textvariable=entry_value_user)
user_entry.grid(row=0, column=1)

button = Button(window, text="Convert", command=convert)
button.grid(row=0, column=2)



text_for_grams = Text(window, height=1, width=20)
text_for_grams.grid(row=1, column=0)

text_for_pounds = Text(window, height=1, width=20)
text_for_pounds.grid(row=1, column=1)

text_for_ounces = Text(window, height=1, width=20)
text_for_ounces.grid(row=1, column=2)



# Prvo se prosledjuje parametar window da bi dugme bilo na prozoru a kasnije ostali parametri. Kod command se ne prosledjuju zagrade kod metode
btn = Button(window, text="Execute", command=miles)
btn.grid(row=2, column=0)

# Sa entry_value uzimamo vrednost iz polja koja je uneta na formi
entry_value = StringVar()
entry = Entry(window, textvariable=entry_value)
entry.grid(row=2, column=1)

text = Text(window, height=1, width=20)
text.grid(row=2, column=2)

window.mainloop()