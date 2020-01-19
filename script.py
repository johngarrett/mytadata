#!/usr/local/bin/python3
import piexif
from os import listdir
from PIL import Image

def update_metadata(dir, image_name, make, model, iso, new_image_name):
    original_dict = piexif.load(f'{dir}/{image_name}')
    x, y = original_dict["0th"][piexif.ImageIFD.XResolution], original_dict["0th"][piexif.ImageIFD.YResolution]

    zeroth_ifd = {piexif.ImageIFD.Make: make,
                  piexif.ImageIFD.Model: model,
                  piexif.ImageIFD.XResolution: x,
                  piexif.ImageIFD.YResolution: y,
                  piexif.ImageIFD.Software: "mytadata"
                  }
    exif_ifd = { piexif.ExifIFD.ISOSpeed: int(iso) }
    first_ifd = zeroth_ifd
    exif_dict = {"0th":zeroth_ifd, "Exif":exif_ifd, "GPS":{}, "1st":first_ifd, "thumbnail":None}
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, f'./{dir}/{new_image_name}')
    print(f'[{image_name} -> {new_image_name}]: Sucess')

def begin(dir):
    new_image_name = input('Enter a name for these photos: ')
    make = input('Enter new make (e.g. Cannon): ')
    model = input('Enter new model (e.g. AE-1): ')
    iso = input('Ener film ISO (e.g. 400): ')
    for (i, file) in enumerate(listdir(dir)):
        try:
            update_metadata(dir, file, make, model, iso, f'{new_image_name}{i}.jpeg')
        except:
            print(f'[{file}]: Error updating metadata')
if __name__=='__main__':
    begin(input("Enter source image directory: "))
