from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter.BLUR)
# filtered_image = img.filter(ImageFilter.SMOOTH)
# filtered_image = img.convert('L')
# print(dir(img))
# print(img.Format)
# print(img.mode)
# print(img.size)
resize = filtered_image.resize((300, 300))
# cropped = (100, 100, 400, 400)
# region = filtered_image.crop(cropped)

# region.save("grey.png", 'png')
resize.save("")
filtered_image.save("grey.png", 'png')
# filtered_image.show()
