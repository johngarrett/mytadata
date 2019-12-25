import piexif
from os import listdir

def update_metadata(path, new_make, new_model):
        exif_dict = piexif.load(path)
        try:
            print(f'\n--------{path}---------')
            print(f'[MODEL]: {exif_dict["0th"][piexif.ImageIFD.Model]}')
            print(f'[MAKE]: {exif_dict["0th"][piexif.ImageIFD.Make]}')
            print(f'[ISO]: {exif_dict["Exif"][piexif.ExifIFD.ISOSpeed]}')

        except:
            print("Key does not exist")
        
            exif_dict["0th"][piexif.ImageIFD.Model]}')
            exif_dict["0th"][piexif.ImageIFD.Make]}')
            exif_dict["Exif"][piexif.ExifIFD.ISOSpeed]}')

def begin(dir):
    make = input('Enter new make: ')
    model = input('Enter new model: ')
    iso = input('Ener film ISO: ')
    for file in listdir(dir):
        update_metadata(f'{dir}/{file}', make, model)
if __name__=='__main__':
    begin("./source_images")
