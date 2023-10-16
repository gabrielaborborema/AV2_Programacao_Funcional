from PIL import Image

image_path = 'imagem_aumentada_brilho.jpg'

img = Image.open(image_path)

width, height = img.size

im_info = lambda : [[img.getpixel((x, y)) for y in range (height)] for x in range (width)]

modified_img_info = lambda funct, iminf : [[tuple (map (funct, iminf[x][y])) for y in range (height)] for x in range (width)]

m = modified_img_info (lambda x : x + 100, im_info (width, height))

update_img = lambda : [[img.putpixel((x, y), m[x][y]) for y in range (height)] for x in range (width)]

update_img()

img.save('imagem_aumentada_brilho.jpg')