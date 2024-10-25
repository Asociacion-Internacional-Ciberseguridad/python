from PIL import Image

imagen = Image.open('imagen.jpg')
imagen.thumbnail((100, 100))
imagen.save('thumbnail.jpg')
