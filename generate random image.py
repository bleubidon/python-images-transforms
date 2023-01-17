import os; os.chdir('C:\\Users\\user\\path\\python_images')
from PIL import Image
from random import randint

img = Image.new('RGB', (500, 500))

for x in range(img.size[0]):
    for y in range(img.size[1]):
        img.putpixel((x, y), (randint(0, 255), randint(0, 255), randint(0, 255)))
        
img.save('random image.png', 'PNG')