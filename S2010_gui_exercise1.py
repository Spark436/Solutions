"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry("100x170")


if __name__ == "__main__":
    main_window.mainloop()