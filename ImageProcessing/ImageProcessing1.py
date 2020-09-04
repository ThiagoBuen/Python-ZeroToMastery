from PIL import Image, ImageFilter

pikachuImg = Image.open('./Pokedex/pikachu.jpg')
astroImg = Image.open('./Resources/astro.jpg')

#filtered_img = pikachuImg.filter(ImageFilter.SHARPEN)
#filtered_img = pikachuImg.convert('L')

#filtered_img.show()
#rotate = filtered_img.rotate(90)
#resize = filtered_img.resize((300,300))
#box = (100,100,400,400)
#region = filtered_img.crop(box)
#region.save("blur.png", 'png')

astroImg.thumbnail((400,200))
astroImg.save('thumbnail.jpg')