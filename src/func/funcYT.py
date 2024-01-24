import yt_dlp

@staticmethod
def on_progress(data, window):
    '''
    Method useful to show the progressBar which fill itself

    Parameters:
    -----------
    data : any
        The amount of data downloaded
    window : mainWindow
        The main window of application
    '''
    if data['status'] == 'finished':
        window.setProgressVar(100)
    else:
        totalSize = data.get('total_bytes', None)
        downloadedSize = data.get('downloaded_bytes', None)

        if totalSize and downloadedSize:
            progress = int((downloadedSize / totalSize) * 100)
            window.setProgressVar(progress)
            window.getWindow().update()

@staticmethod
def downloadAudio(videoUrl, outputPath, window):
    '''
    Method which download a file audio (mp3) of the video passed as parameter. Return true if the download has gone ok, false otherwise

    Parameters:
    -----------
    videoUrl : str
        The Url of youtube video to download
    outputPath : str
        The path where the file will be downloaded
    window : mainWindow
        The main window of the application

    Returns:
    --------
    boolean:
        It's true if the download has gone ok, false otherwise
    '''
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # get only the audio
        'audioformat': 'mp3',  # specify the format of file
        'outtmpl': f'{outputPath}/%(title)s.mp3',
        'progress_hooks': [lambda d: on_progress(d, window)]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([videoUrl])

        return True
    except Exception as e:
        print("Error during the download\n")
        print(e)
        return False
    
@staticmethod
def downloadVideo(videoUrl, outputPath, window):
    '''
    Method which download a file video (mp4) of the video passed as parameter. Return true if the download has gone ok, false otherwise

    Parameters:
    -----------
    videoUrl : str
        The Url of youtube video to download
    outputPath : str
        The path where the file will be downloaded
    window : mainWindow
        The main window of the application

    Returns:
    --------
    boolean:
        It's true if the download has gone ok, false otherwise
    '''
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': f'{outputPath}/%(title)s.mp4',
            'progress_hooks': [lambda d: on_progress(d, window)]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(videoUrl, download=True)

        return True
    except Exception as e:
        print("Error during the download\n")
        print(e)
        return False
    



