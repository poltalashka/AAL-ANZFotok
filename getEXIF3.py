from PIL import Image
from PIL.ExifTags import TAGS


#1 Recursively Traverse thru folders  
#2 find each image ( jpg, JPG, png, PNG) 
#3 Save the file name, path, dimensions, EXIF details, image-signature   
#4 In SQlite-DB
#5 Identify Faces, add face info to Qlite-DB

image = Image.open('sammy.jpg')

exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:

    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")

    #(als_Foto) C:\palashworld\_dev\HOME_PY\als_Foto>python getEXIF3.py
    #ImageWidth               : 3840
    #ImageLength              : 2160
    #GPSInfo                  : 902
    #ResolutionUnit           : 2
    #ExifOffset               : 245
    #Make                     : Google
    #Model                    : Pixel 3 XL
    #Software                 : HDR+ 1.0.362396382zd
    #Orientation              : 6
    #DateTime                 : 2021:04:15 20:22:10
    #YCbCrPositioning         : 1
    #XResolution              : 72.0
    #YResolution              : 72.0