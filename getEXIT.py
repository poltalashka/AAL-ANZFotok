from exif import Image

with open('sammy.jpg', 'rb') as image_file: 
    my_image = Image(image_file)
    #print( my_image.size())
    my_image.has_exif
    print( my_image.list_all())
