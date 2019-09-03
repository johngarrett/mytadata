import piexif
from os import listdir

for image in listdir("./source_images"):
    exif_dict = piexif.load("./source_images/"+image)
    try:
        print(f'\n--------{image}---------')
        print(f'[MODEL]: {exif_dict["0th"][piexif.ImageIFD.Model]}')
        print(f'[MAKE]: {exif_dict["0th"][piexif.ImageIFD.Make]}')
        print(f'[ISO]: {exif_dict["Exif"][piexif.ExifIFD.ISOSpeed]}')

    except:
        print("Key does not exist")
