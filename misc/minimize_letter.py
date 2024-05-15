import PIL
from PIL import Image
def get_letters():
    image = Image.open('screenshot.png')
    cropped_image = image.crop((120, 648, 618, 1152))
    cropped_image.save('cropped_letters.png')
    print("Cropped letters saved.")


get_letters()