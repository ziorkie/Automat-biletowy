from tkinter import *
from Window import *


def main():
    try:
        root = Tk()
        app = Application(master=root)
        root.resizable(0,0)
        app.mainloop()

    except:
        messagebox.showerror("błąd tworzenia aplikacji!","coś poszło nie tak...")
        pass
if __name__=="__main__":
    main()