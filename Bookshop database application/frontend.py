from tkinter import *
import backend

# Prosledjuje se event koji sadrzi informacije o eventu (za bajndovanje)
def get_selected_row(event):
    try:
        # Global oznacava da je globalna promenljiva iako je definisana u metodi, bice vidljiva svuga u programu
        global selected_tuple
        # Metod curselection daje id trenutnog reda a get() daje tuple odnosno sve podatke iz tog zapisa (reda)
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        title_text.delete(0, END)
        title_text.insert(END, selected_tuple[1])
        author_text.delete(0, END)
        author_text.insert(END, selected_tuple[2])
        year_text.delete(0, END)
        year_text.insert(END, selected_tuple[3])
        isbn_text.delete(0, END)
        isbn_text.insert(END, selected_tuple[4])
    except IndexError:
        pass



def view_command():
    # Prvo obrisemo sve od 0 do kraja reda a onda dodajemo zapise u listu
    list_box.delete(0, END)
    for row in backend.view():
        list_box.insert(END, row)


def search_command():
    list_box.delete(0, END)
    # Mora da se stavi get metod zato sto iz polja uzima StringVar koji nije plain string
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)


def insert_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0, END)
    list_box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("Book store")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

title_text_input = StringVar()
title_text = Entry(window, textvariable=title_text_input)
title_text.grid(row=0, column=1)

author_text_input = StringVar()
author_text = Entry(window, textvariable=author_text_input)
author_text.grid(row=0, column=3)

year_text_input = StringVar()
year_text = Entry(window, textvariable=year_text_input)
year_text.grid(row=1, column=1)

isbn_text_input = StringVar()
isbn_text = Entry(window, textvariable=isbn_text_input)
isbn_text.grid(row=1, column=3)

list_box = Listbox(window, height=6, width=35)
# rowspan i columnspan za prosirenje list box-a
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)
# Kaze da scroll bar prati y osu list box-a
list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

view_all_button = Button(window, text="View all", width=12, command=view_command)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(window, text="Search entry", width=12, command=search_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text="Add entry", width=12, command=insert_command)
add_entry_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()