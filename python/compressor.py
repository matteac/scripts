from PIL import Image
import os

picturesFolder = "/home/" + os.getlogin() + "/Pictures/"
compressedFolder = "/home/" + os.getlogin() + "/Pictures/Compressed/"

if __name__ == "__main__":
    for filename in os.listdir(picturesFolder):
        name, extension = os.path.splitext(picturesFolder + filename)

        if extension in [".jpeg", ".jpg", ".png"]:
            pic = Image.open(picturesFolder + filename)
            pic.save(compressedFolder + "compressed_" + filename, optimize=True, quality=50)
