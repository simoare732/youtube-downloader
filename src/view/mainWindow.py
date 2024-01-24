import tkinter as tk 
from tkinter import ttk
from func.downloadListener import downloadBut

nameOfFile = "vid"

class mainWindow:
    """
    The class which represent the main window of the application

    Attributes:
    -----------
    window : tK
        The window of the application
    textField : Entry
        A text field where the user can write the URL of the video
    comboBox : ComboBox
        A combobox to choose the format of the video (mp3 or mp4)
    progressVar : IntVar
        The variable which change during the download of the video
    progressBar : Progressbar
        The widget which shows us the progress of the download
    downlBut : Button
        The button to download the file

    

    Methods:
    --------
    getWindow():
        Return the window of the application
    getProgressVar():
        Return the Variable of the progress bar of the download
    setProgressVar(value):
        Set the progressVar to value
    getProgressBar():
        Return the widget of progress bar
    """

    def __init__(self, size, title):
        self.window = tk.Tk()
        self.window.geometry(size)
        self.window.title(title)
        self.window.minsize(width=510, height=200)
        self.window.grid_columnconfigure(0, weight=1)

        introductLabel = tk.Label(self.window, font=("Helvetica", "13"), text="Insert youtube URL and choose what type of file you want to download")
        introductLabel.grid(row=0, column=0, sticky="n", pady=5)

        self.textField = tk.Entry(self.window, width=50, font=(25))
        self.textField.grid(row=1, column=0, sticky="we", pady=10, padx=5)

        options = [".mp3 (audio)", ".mp4 (video)"]
        self.comboBox = ttk.Combobox(self.window, values=options, font=(8))
        self.comboBox.set("Select the type of the file")
        self.comboBox.config(state="readonly")
        self.comboBox.grid(row=2, column=0, padx=5)

        self.progressVar = tk.IntVar()
        self.progressBar = ttk.Progressbar(self.window, length=400, variable=self.progressVar, mode="determinate")
        self.progressBar.grid(row=4, column=0, sticky="s")
        self.progressBar.grid_remove()

        self.downlBut = tk.Button(self.window, text="Download", font=(25), command=lambda: downloadBut(self.comboBox, nameOfFile, self.textField.get(), self), background="#CC0000", foreground="white")
        self.downlBut.grid(row=3, column=0, sticky="s", pady=10)

    
    def getWindow(self):
        '''
        Return the window of the application
        '''
        return self.window
    
    def getProgressVar(self):
        '''
        Return the Variable of the progress bar of the download       
        '''
        return self.progressVar

    def setProgressVar(self, value):
        '''
        Set the progressVar to value

        Parameters:
        -----------
        value : int
            The new value of progressVar
        '''
        self.progressVar.set(value)
    
    def getProgressBar(self):
        '''
        Return the widget of progress bar
        '''
        return self.progressBar
