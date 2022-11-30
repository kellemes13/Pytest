from PIL import Image

Image_file=Image.open("SendTotutorial.png")
Image_file=Image_file.convert('1')
Image_file.save('result.png')