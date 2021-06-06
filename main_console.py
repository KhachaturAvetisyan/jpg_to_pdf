from PIL import Image

image1 = Image.open(r'E:\Python\bots\jpg_to_pdf\imj\kodzik4.PNG')
im1 = image1.convert('RGB')
im1.save(r'E:\Python\bots\jpg_to_pdf\imj\FirstImage.pdf')
