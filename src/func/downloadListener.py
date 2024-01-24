from .funcYT import *

import tkinter as tk
from tkinter import messagebox

import os

@staticmethod
def createDirectory(name):
    '''
    A method to create a directory called name. Inside of it, will be the file downloaded

    Parameters:
    ------------
    name : str
        The name of directory created
    
    Returns:
    ---------
    dirCreated : str
        The absolute path of the directory created
    '''

    #get the path of current directory
    currentDir = os.getcwd()

    #create the complete path for the directory called name
    dirCreated = os.path.join(currentDir, name)

    #verify wheter the directory exist or not
    if not os.path.exists(dirCreated):
        os.makedirs(dirCreated)
    
    return dirCreated


@staticmethod
def downloadBut(cB, name, videoUrl, window):
    '''
    A method which manage the press of download button. When it is pressed, the file starts to download

    Parameters:
    -----------
    cB : comboBox
        The comboBox of application
    name : str
        The name of directory which will be create
    videoUrl : str
        The url of youtube video to download
    window : mainWindow
        The main window of application 
    '''
    ext = cB.get()
    path = createDirectory(name)
    res = False
    window.setProgressVar(0)
    window.getProgressBar().grid()
    window.getWindow().update()
    if ext == ".mp3 (audio)":
        res = downloadAudio(videoUrl, path, window)
    elif ext == ".mp4 (video)":
        res = downloadVideo(videoUrl, path, window)
    
    if not res:
        messagebox.showerror("Messaggio", "Insert a valid URL")

    window.getProgressBar().grid_remove()


