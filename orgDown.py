import os 

downloadFolder = "/home/" + os.getlogin() + "/Downloads/"
picturesFolder = "/home/" + os.getlogin() + "/Pictures/"
musicFolder = "/home/" + os.getlogin() + "/Music/"

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        if extension in [".jpeg", ".jpg", ".png"]:
            os.rename(downloadFolder + filename, picturesFolder + filename)
        
        if extension in [".mp3", ".wav"]:
            os.rename(downloadFolder + filename, musicFolder + filename)