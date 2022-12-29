from PIL import Image
import glob


img_file = '/home/dell/Desktop/images'
img_list = glob.glob(img_file + '/*.png')

for i in img_list:
    img = Image.open(i)
    
    img_name = (i.split('.')[0]).split('/')[-1]+'.jpg'
    img.save('/home/dell/Desktop/output/' + img_name, 'JPEG')

