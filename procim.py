from PIL import Image, ImageFilter

img = Image.open('./downloads/astro.jpg')
# # new_img = img.resize((400, 400))
# new_img = img
# new_img.save('thumbnail.py')
img.thumbnail(400, 400)
img.save('thumbnail.jpg')
img.show()
