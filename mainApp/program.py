from PIL import Image
import glob, os

# for infile in glob.glob('/media/konan.jpeg'):
#     file, ext = os.path.splitext(infile)
#     with Image.open(infile) as im:
#         im.thumbnail(size)
#         im.save(file + "konan.thumbnail", "JPEG")

# img = Image.open('media/konan.jpeg')

# size = (200, 200)
# img.thumbnail(size)
# img.save('konan_thumbnail.jpeg')

def tnails():
    try:
        image = Image.open('media/konan.jpeg')
        image.thumbnail((300,300))
        image.save('media/konan_thumbnail.jpeg')
        image1 = Image.open('media/konan_thumbnail.jpeg')
        image1.show()
    except IOError:
        pass
tnails()