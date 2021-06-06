import img2pdf
import glob

# global im1
#
# image_list = []

file = open("./photos/test.pdf", "wb")
file.write((img2pdf.convert(glob.glob('./photos/*.jpg'))))
file.close()

# for filename in glob.glob('./photos/*.jpg'):
#     image1 = Image.open(filename)
#     im1 = image1.convert('RGB')
#     image_list.append(im1)
# im1.save('./photos/test.pdf', save_all=True, append_images=image_list)

# files = glob.glob('./photos/*')
# for f in files:
# os.remove(f)
