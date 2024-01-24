import tkinter as tk
from view.mainWindow import mainWindow 


if __name__ == "__main__":
    mainW = mainWindow("700x450", "Youtube downloader")
    mainW.getWindow().mainloop()