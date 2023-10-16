from PIL import Image, ImageEnhance

image = Image.open("imagem.jpg")

brilho_factor = 3

aumentar_brilho = ImageEnhance.Brightness(image).enhance(brilho_factor)
aumentar_brilho.save("imagem_aumentada_brilho.jpg")

image.close()
