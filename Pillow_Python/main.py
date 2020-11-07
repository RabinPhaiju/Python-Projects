from PIL import Image, ImageFilter

img = Image.open('files/2.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

# print(dir(img)) 

# img_new = img.filter(ImageFilter.BLUR) # blur
# img_new = img.convert('L') # grayscale
# img_new = img.rotate(180) # rotate
# img_new = img.resize((300, 300)) 3 resize
img_new = img.crop((100,100,200,200)) # crop


img_new.save('new.png') # change extension to change file type