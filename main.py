from tkinter import *
from Window import *


def main():
    try:
        root = Tk()
        app = Application(master=root)
        root.resizable(0,0)
        app.mainloop()

    except:
        #popupmsg("Błąd\ntworzenia \nw main")
        pass
if __name__=="__main__":
    main()