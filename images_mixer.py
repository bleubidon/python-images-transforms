import os; os.chdir('C:\\Users\\user\\Desktop\\fd')
from PIL import Image

image_1 = 'fan_inverted.jpg'
image_2 = 'tech.jpg'

image_1_list, image_2_list, image_mixed_list = [], [], []

img = Image.open(image_1)
width = img.size[0]
height = img.size[1]

for y in range(height):
    image_1_list.append([])
    image_2_list.append([])
    image_mixed_list.append([])
for x in range(width):
    for i in range(len(image_1_list)):
        image_1_list[i].append([])
        image_2_list[i].append([])
        image_mixed_list[i].append([])

for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        image_1_list[y][x].append(r)
        image_1_list[y][x].append(g)
        image_1_list[y][x].append(b)
        
img = Image.open(image_2)
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        image_2_list[y][x].append(r)
        image_2_list[y][x].append(g)
        image_2_list[y][x].append(b)
        
#print(image_1_list)
#print(image_2_list)

for x in range(width):
    for y in range(height):
        pxl_r1 = image_1_list[y][x][0];pxl_g1 = image_1_list[y][x][1];pxl_b1 = image_1_list[y][x][2]
        pxl_r2 = image_2_list[y][x][0];pxl_g2 = image_2_list[y][x][1];pxl_b2 = image_2_list[y][x][2]
        
        r, g, b = round((pxl_r1 + pxl_r2) /2), round((pxl_g1 + pxl_g2) /2), round((pxl_b1 + pxl_b2) /2)
        
        image_mixed_list[y][x].append(r)
        image_mixed_list[y][x].append(g)
        image_mixed_list[y][x].append(b)
        
#print(image_mixed_list)        

img = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        img.putpixel((x, y), (image_mixed_list[y][x][0], image_mixed_list[y][x][1], image_mixed_list[y][x][2]))
        
img.save('fan_inverted_tech.jpg', 'JPEG')