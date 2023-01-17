# import os; os.chdir('C:\\Users\\user\\path\\python_images')
import os; os.chdir('C:\\Users\\user\\Desktop')
from PIL import Image
from copy import deepcopy

def copied_str(image_list):
    image_list_copied = []
    for i in range(len(image_list)):
        image_list_copied.append([])
    for i in range(len(image_list)):
        for j in range(len(image_list[0])):
            image_list_copied[i].append([])
            
    return image_list_copied

def sliced_image(image):
    image_list = []
    
    img = Image.open(image)
    width = img.size[0]
    height = img.size[1]
    
    for y in range(height):
        image_list.append([])
    for x in range(width):
        for i in range(len(image_list)):
            image_list[i].append([])
    
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            image_list[y][x].append(r)
            image_list[y][x].append(g)
            image_list[y][x].append(b)

    return image_list
    
def rebuilt_image(image_list):
    width = len(image_list[0])
    height = len(image_list)
    
    img = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            img.putpixel((x, y), (image_list[y][x][0], image_list[y][x][1], image_list[y][x][2]))
    
    return img
    
def mixed_images(image_list_1, image_list_2, degree_1, degree_2):
    image_list_mixed = copied_str(image_list_1)
    
    for x in range(len(image_list_1[0])):
        for y in range(len(image_list_1)):
            pxl_r1 = image_list_1[y][x][0];pxl_g1 = image_list_1[y][x][1];pxl_b1 = image_list_1[y][x][2]
            pxl_r2 = image_list_2[y][x][0];pxl_g2 = image_list_2[y][x][1];pxl_b2 = image_list_2[y][x][2]
            
            r, g, b = round((pxl_r1*degree_1 + pxl_r2*degree_2) /(degree_1+degree_2)), round((pxl_g1*degree_1 + pxl_g2*degree_2) /(degree_1+degree_2)), round((pxl_b1*degree_1 + pxl_b2*degree_2) /(degree_1+degree_2))
            
            image_list_mixed[y][x].append(r)
            image_list_mixed[y][x].append(g)
            image_list_mixed[y][x].append(b)
    
    return image_list_mixed
    
def modified_colours(image_list, colours_list, degrees_list, modes_list):    
    image_list_intensified = deepcopy(image_list)
    
    for i in range(len(image_list)):
        for j in range(len(image_list[i])):
            for k in range(len(colours_list)):
                old = image_list[i][j][colours_list[k]]
                if modes_list[k] == 1:new = round((255-old) /100 * degrees_list[k] + old)
                elif modes_list[k] == 0: new = round(-old /100 * degrees_list[k] + old)
                         
                image_list_intensified[i][j][colours_list[k]] = new
        
    return image_list_intensified

def reversed_colours(image_list):
    image_list_complemented = deepcopy(image_list)
    for i in range(len(image_list)):
        for j in range(len(image_list[0])):
            for k in range(3):
                image_list_complemented[i][j][k] = 255 - image_list[i][j][k]
            
    return image_list_complemented
    
def inverted_colours_order(image_list, order):
    image_list_inverted = deepcopy(image_list)
    for i in range(len(image_list)):
        for j in range(len(image_list[0])):
            for k in range(3):
                image_list_inverted[i][j][k] = image_list[i][j][order[k]]
                
    return image_list_inverted

'''image_name = 'original.jpg'

rebuilt_image(modified_colours(sliced_image(image_name), [0], [100], [0])).save('but_red.jpg', 'JPEG');print('done : 1')
rebuilt_image(modified_colours(sliced_image(image_name), [1], [100], [0])).save('but_green.jpg', 'JPEG');print('done : 2')
rebuilt_image(modified_colours(sliced_image(image_name), [2], [100], [0])).save('but_blue.jpg', 'JPEG');print('done : 3')

rebuilt_image(modified_colours(sliced_image(image_name), [0, 1], [100, 100], [0, 0])).save('blue.jpg', 'JPEG');print('done : 4')
rebuilt_image(modified_colours(sliced_image(image_name), [0, 2], [100, 100], [0, 0])).save('green.jpg', 'JPEG');print('done : 5')
rebuilt_image(modified_colours(sliced_image(image_name), [1, 2], [100, 100], [0, 0])).save('red.jpg', 'JPEG');print('done : 6')

rebuilt_image(modified_colours(sliced_image(image_name), [0], [100], [1])).save('more_red.jpg', 'JPEG');print('done : 7')
rebuilt_image(modified_colours(sliced_image(image_name), [1], [100], [1])).save('more_green.jpg', 'JPEG');print('done : 8')
rebuilt_image(modified_colours(sliced_image(image_name), [2], [100], [1])).save('more_blue.jpg', 'JPEG');print('done : 9')

#######################################

rebuilt_image(inverted_colours_order(sliced_image(image_name), [0, 2, 1])).save('021.jpg', 'JPEG');print('done : 10')
rebuilt_image(inverted_colours_order(sliced_image(image_name), [1, 0, 2])).save('102.jpg', 'JPEG');print('done : 11')
rebuilt_image(inverted_colours_order(sliced_image(image_name), [1, 2, 0])).save('120.jpg', 'JPEG');print('done : 12')
rebuilt_image(inverted_colours_order(sliced_image(image_name), [2, 0, 1])).save('201.jpg', 'JPEG');print('done : 13')
rebuilt_image(inverted_colours_order(sliced_image(image_name), [2, 1, 0])).save('210.jpg', 'JPEG');print('done : 14')

#######################################
#######################################

rebuilt_image(reversed_colours(sliced_image('original.jpg'))).save('reversed_original.jpg', 'JPEG');print('done : 15')

rebuilt_image(reversed_colours(sliced_image('but_red.jpg'))).save('reversed_but_red.jpg', 'JPEG');print('done : 16')
rebuilt_image(reversed_colours(sliced_image('but_green.jpg'))).save('reversed_but_green.jpg', 'JPEG');print('done : 17')
rebuilt_image(reversed_colours(sliced_image('but_blue.jpg'))).save('reversed_but_blue.jpg', 'JPEG');print('done : 18')

rebuilt_image(reversed_colours(sliced_image('blue.jpg'))).save('reversed_blue.jpg', 'JPEG');print('done : 19')
rebuilt_image(reversed_colours(sliced_image('green.jpg'))).save('reversed_green.jpg', 'JPEG');print('done : 20')
rebuilt_image(reversed_colours(sliced_image('red.jpg'))).save('reversed_red.jpg', 'JPEG');print('done : 21')

rebuilt_image(reversed_colours(sliced_image('more_red.jpg'))).save('reversed_more_red.jpg', 'JPEG');print('done : 22')
rebuilt_image(reversed_colours(sliced_image('more_green.jpg'))).save('reversed_more_green.jpg', 'JPEG');print('done : 23')
rebuilt_image(reversed_colours(sliced_image('more_blue.jpg'))).save('reversed_more_blue.jpg', 'JPEG');print('done : 24')

######################################

rebuilt_image(reversed_colours(sliced_image('021.jpg'))).save('reversed_021.jpg', 'JPEG');print('done : 25')
rebuilt_image(reversed_colours(sliced_image('102.jpg'))).save('reversed_102.jpg', 'JPEG');print('done : 26')
rebuilt_image(reversed_colours(sliced_image('120.jpg'))).save('reversed_120.jpg', 'JPEG');print('done : 27')
rebuilt_image(reversed_colours(sliced_image('201.jpg'))).save('reversed_201.jpg', 'JPEG');print('done : 28')
rebuilt_image(reversed_colours(sliced_image('210.jpg'))).save('reversed_210.jpg', 'JPEG');print('done : 29')

##Examples make the manual !
#######################################
#######################################'''

image_1 = 'ii.jpg'
rebuilt_image(modified_colours(sliced_image(image_1), [0], [100], [0])).save('but_red.jpg', 'JPEG')











